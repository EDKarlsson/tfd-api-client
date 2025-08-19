#!/usr/bin/env bash
cmd=$1

CHILD_SCHEMAS=(recommendation user)
JOINED_API=spec/tfd.openapi.yaml

for api in "${CHILD_SCHEMAS[@]}"; do
    api_file=${api}.openapi.yaml
    sed "s/ErrorMessage/${api}ErrorMessage/" spec/${api_file} > spec/tmp-${api_file}
done

redocly join -o ${JOINED_API}

for api in "${CHILD_SCHEMAS[@]}"; do
    sed -i.bu-${api} "/${api}ErrorMessage:/,+11d" ${JOINED_API}
    sed -i.bu-${api}-1 "s/${api}ErrorMessage/ErrorMessage/" ${JOINED_API}
done

rm .bu* spec/tmp-*
sed -i.'' 's/MetaData/Metadata/g' ${JOINED_API}