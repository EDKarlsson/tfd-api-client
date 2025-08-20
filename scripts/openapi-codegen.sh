#/usr/bin/env bash

PACKAGE_VERSION=1.0.0
PROJECT_NAME=tfd-api-client

# Available generators: python, python-pydantic-v1, python-fastapi, go, go-server.
OPENAPI_GENERATOR=python
OPENAPI_CONFIG=openapi-codegen.yaml
OPENAPI_PREPROCESS=scripts/preprocess_openapi.py

SPEC_DIR=spec
OPENAPI_SPEC=tfd.openapi.yaml
OPENAPI_FILE=$SPEC_DIR/$OPENAPI_SPEC

preprocess() {
  python $OPENAPI_PREPROCESS
  mv -v ${OPENAPI_FILE} ${OPENAPI_FILE}.bu
  mv -v out/staged-openapi.yaml $SPEC_DIR/$OPENAPI_SPEC
}

codegen() {
  echo "openapi-gen ${OPENAPI_GENERATOR} ${OPENAPI_SPEC}"
  docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/${OPENAPI_FILE} \
    -c /local/${OPENAPI_CONFIG} \
    -p ${PACKAGE_VERSION} \
    -g ${OPENAPI_GENERATOR} \
    -o /local/out/${OPENAPI_GENERATOR}-client
}

case "$1" in
  pre)
    echo "Running preprocessing"
    preprocess
    ;;
  gen)
    echo "Running default codegen"
    codegen
    ;;
  *)
    echo "run with cmds: ${1}"
    docker run --rm \
      -v ${PWD}:/local openapitools/openapi-generator-cli $@
    ;;
esac