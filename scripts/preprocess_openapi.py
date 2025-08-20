import yaml
import argparse
import re
import logging
import logging.config
from pathlib import Path
from typing import Callable

logger = logging.getLogger("preprocessor")
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Example usage:
SPEC_DIR = PROJECT_ROOT / "spec"
CONFIG_DIR = PROJECT_ROOT / "configs"


def process(spec_file: str, conf_file: str) -> dict:
    with open(conf_file, "r") as cf, open(spec_file, "r") as mds:
        config_yml = yaml.load(cf, Loader=yaml.FullLoader)
        openapi_yml = yaml.load(mds, Loader=yaml.FullLoader)

    openapi_spec = process_api(openapi_yml, config_yml)
    return openapi_spec


def simplify_path(path_str: str) -> str:
    return (
        path_str.replace("/static/tfd/", "")
        .replace("/{language_code}", "")
        .replace("/tfd/v1/", "")
        .replace(".json", "")
    )


def make_plural(instr: str) -> str:
    return instr + "s" if instr[-1] != "s" else instr


def format_operation_id(path_str: str, plural: bool) -> str:
    operation_id = re.sub(r"[-/]", " ", path_str)
    operation_id = "get" + operation_id.title().replace(" ", "")
    operation_id = make_plural(operation_id) if plural else operation_id
    return operation_id


def get_schema_ref(response_ref: dict) -> str:
    return response_ref["get"]["responses"]["200"]["content"]["application/json"][
        "schema"
    ]["$ref"]


def set_schema_ref(path_obj: dict, reference:str)->dict:
    path_obj["get"]["responses"]["200"]["content"]["application/json"]["schema"][
        "$ref"
    ] = reference
    return path_obj


def format_response(response_str: str, plural: bool = True) -> str:
    suffix = "s" if plural else ""
    return response_str.replace("Response", suffix)


def regex_flag(
    re_method: Callable[[str, str], bool], config: dict, option: str, string: str
) -> bool:
    return True if re_method("|".join(config[option]), string) else False


def search_flag(config: dict, option: str, string: str) -> bool:
    return regex_flag(re.search, config, option, string)


def match_flag(config: dict, option: str, string: str) -> bool:
    return regex_flag(re.match, config, option, string)


def process_api(openapi_spec: dict, config: dict)->dict:
    api_paths = openapi_spec["paths"]
    conf_path = config["paths"]
    conf_general = config["general"]
    conf_schemas = config["schemas"]
    for k in list(api_paths.keys()):
        # Changes path from /foo/bar/{baz}/boo[.json] to bar/boo[.json]
        path = simplify_path(k)
        logger.debug(f"path: {path}")

        if path in conf_path:
            operationId = format_operation_id(conf_path[path], plural=False)
        else:
            plural_flag = search_flag(conf_general, "set-plural", path)
            operationId = format_operation_id(path, plural=plural_flag)
            logger.debug(f"Set operationId -> {operationId}")
            api_paths[k]["get"]["operationId"] = operationId

        schema_ref = get_schema_ref(api_paths[k])
        old_component = schema_ref.split("/")[-1]
        plural_flag = not match_flag(conf_schemas, "skip", old_component)
        response_ref = format_response(schema_ref, plural_flag)
        new_component = response_ref.split("/")[-1]

        # Skip any
        # if not match_flag(conf_schemas, "skip", old_component):
        if old_component != new_component:

            openapi_spec["components"]["schemas"][new_component] = openapi_spec[
                "components"
            ]["schemas"].pop(old_component)

        logger.debug(f"Component old,new: {old_component} -> {new_component}")
        logger.debug(f"Set $ref -> {response_ref}\n")

        openapi_spec["paths"][k] = set_schema_ref(api_paths[k], response_ref)
    return openapi_spec

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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
        "--verbose", "-v", help="display debug information", action="store_true"
    )
    parser.add_argument(
        # "--log-config", help="Set python logging config", default="logging.conf"
        "--log-config",
        help="Set python logging config",
        default="logging.yaml",
    )
    args = parser.parse_args()

    with open(f"{CONFIG_DIR}/{args.log_config}", "rt") as lcf:
        log_conf = yaml.safe_load(lcf.read())
        logging.config.dictConfig(log_conf)
    if args.verbose:
        logger.info("Verbose Output")
        logger.setLevel(logging.DEBUG)

    conf_file = f"{CONFIG_DIR}/{args.config}"
    spec_file = f"{SPEC_DIR}/{args.spec}"

    openapi_spec = process(spec_file=spec_file, conf_file=conf_file)

    if not args.dry:
        with open("./out/staged-schemas.openapi.yaml", "w") as md_fyml:
            yaml.dump(openapi_spec, md_fyml, sort_keys=False)
    # else:
    #     print(yaml.dump(openapi_spec))
