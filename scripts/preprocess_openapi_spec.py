import yaml
import argparse


def main():
    conf_file = "configs/datamodel.conf.yaml"
    spec_file = "spec/nexon/metadata.openapi.yaml"
    conf_yml = None
    metadata_yml = None

    with open(conf_file, "r") as cf:
        conf_yml = yaml.load(cf, Loader=yaml.FullLoader)

    with open(spec_file, "r") as mds:
        metadata_yml = yaml.load(mds, Loader=yaml.FullLoader)
        schemas_prop = metadata_yml["components"]["schemas"]
        for k in list(schemas_prop.keys()):
            nk = conf_yml["metadata"].get(k, None)
            if nk:
                # print(f"Key: {k} ==> {nk}")
                schemas_prop[nk] = schemas_prop.pop(k)
        metadata_yml["components"]["schemas"] = schemas_prop
        print(f"Updated {len(schemas_prop.keys())} of keys...")

    with open("./out/specs/metadata.openapi.yaml", "w") as md_fyml:
        yaml.dump(metadata_yml, md_fyml)


if __name__ == "__main__":
    main()
