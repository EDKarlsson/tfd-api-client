import yaml
import argparse
import re
import logging
import logging.config
import os
from pathlib import Path

logger = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Example usage:
SPEC_DIR = PROJECT_ROOT / "spec"
CONFIG_DIR = PROJECT_ROOT / "configs"


def ymlprint(ymlobj):
    print(yaml.dump(ymlobj))


def preprocess(spec_file, conf_file):
    with open(conf_file, "r") as cf, open(spec_file, "r") as mds:
        config_yml = yaml.load(cf, Loader=yaml.FullLoader)
        openapi_yml = yaml.load(mds, Loader=yaml.FullLoader)

    openapi_spec = process_paths(openapi_yml, config_yml)
    return openapi_spec


def simplify_path(path_str: str) -> str:
    return (
        path_str.replace("/static/tfd/", "")
        .replace("/{language_code}", "")
        .replace("/tfd/v1/", "")
        .replace(".json", "")
    )


def format_operation_id(path_str: str, make_plural: bool) -> str:
    operation_id = re.sub(r"[-/]", " ", path_str)
    operation_id = "get" + operation_id.title().replace(" ", "")
    if make_plural and operation_id[-1] != "s":
        operation_id += "s"
    return operation_id


def get_schema_ref(response_ref) -> str:
    return response_ref["get"]["responses"]["200"]["content"]["application/json"][
        "schema"
    ]["$ref"]


def set_schema_ref(path_obj, ref_string):
    path_obj["get"]["responses"]["200"]["content"]["application/json"]["schema"][
        "$ref"
    ] = ref_string
    return path_obj


def format_response(response_str: str, make_plural: bool = True) -> str:
    plural = "s" if make_plural else ""
    return response_str.replace("Response", plural)


def process_paths(openapi_spec, config):
    api_paths = openapi_spec["paths"]
    custom = config["paths"]
    for k in list(api_paths.keys()):
        # Changes path from /foo/bar/{baz}/boo[.json] to bar/boo[.json]
        path = simplify_path(k)
        logger.debug(f"path: {path}")

        has_op_id = api_paths[k]["get"].get("operationId", None)
        if not has_op_id:
            logger.info("missing op id")
            if path in custom.keys():
                operationId = format_operation_id(custom[path], make_plural=False)
            else:
                if path.split("/")[0] in config["general"]["set-plural"]:
                    operationId = format_operation_id(path, make_plural=True)
                else:
                    operationId = format_operation_id(path, make_plural=False)

            logger.info(f"Set operationId->{operationId}")
            api_paths[k]["get"]["operationId"] = operationId

        response_ref = format_response(get_schema_ref(api_paths[k]))
        logger.debug(f"Set $ref->{response_ref}\n")
        openapi_spec["paths"][k] = set_schema_ref(api_paths[k], response_ref)

    return openapi_spec


def process_schemas(openapi_spec, config):
    schemas_prop = openapi_spec["components"]["schemas"]
    for k in list(schemas_prop.keys()):
        nk = config["metadata"].get(k, None)
        if nk:
            schemas_prop[nk] = schemas_prop.pop(k)
    openapi_spec["components"]["schemas"] = schemas_prop
    print(f"Updated {len(schemas_prop.keys())} of keys...")
    return openapi_spec


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("target", choices=["datamodel","openapi"], help="Select to preprocess spec file for either Pydantics datamodel codegen, or openapi codegen for client.")
    parser.add_argument(
        "--dry",
        action="store_true",
        help="Do not write any files, only output the changes.",
    )
    parser.add_argument(
        "--config", "-c", help="App config file", default="preprocess.conf.yaml"
    )
    parser.add_argument(
        "--spec", "-s", help="OpenAPI Specification File", default="tfd.openapi.yaml"
    )
    parser.add_argument(
        "--log-config", help="Set python logging config", default="logging.conf"
    )

    args = parser.parse_args()

    conf_file = f"{CONFIG_DIR}/{args.config}"
    spec_file = f"{SPEC_DIR}/{args.spec}"

    logging.config.fileConfig(f"{CONFIG_DIR}/{args.log_config}")

    openapi_spec = preprocess(spec_file=spec_file, conf_file=conf_file)

    if not args.dry:
        with open("./out/staged-schemas.openapi.yaml", "w") as md_fyml:
            yaml.dump(openapi_spec, md_fyml)
    # else:
    #     print(yaml.dump(openapi_spec))
