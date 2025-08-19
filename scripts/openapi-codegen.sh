#/usr/bin/env bash

COMMAND=$1

PACKAGE_VERSION=1.0.0
PROJECT_NAME=tfd-api-client

# Available generators: python, python-pydantic-v1, python-fastapi, go, go-server.
OPENAPI_GENERATOR=python
OPENAPI_CONFIG=configs/openapi-codegen.yaml

NEXON_SCHEMA_DIR=spec
NEXON_OPENAPI_SCHEMA=tfd.openapi.yaml

if [ -z $COMMAND ]; then
  echo "openapi-gen ${OPENAPI_GENERATOR} ${NEXON_OPENAPI_SCHEMA}"
  docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/${NEXON_SCHEMA_DIR}/${NEXON_OPENAPI_SCHEMA} \
    -c /local/${OPENAPI_CONFIG} \
    -p ${PACKAGE_VERSION} \
    -g ${OPENAPI_GENERATOR} \
    -o /local/out
    # -o /local/out/${PROJECT_NAME}
else
  echo "run with cmds: ${@}"
  docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli $@
fi