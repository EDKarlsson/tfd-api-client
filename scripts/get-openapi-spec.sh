#!/bin/bash

HTML_FILE=tfd-page.html
NEXON_API_UI_URL="https://openapi.nexon.com/game/tfd/?id=21"
NEXON_API_ROOT_URL=https://openapi.nexon.com/static/api/tfd


curl -X 'GET' \
  $NEXON_API_UI_URL \
  -H 'accept: application/json' \
  -H "$NEXON_API_KEY" > $HTML_FILE

SPEC_FILES=( $(grep -o -m 1 -E "2[0-9]_en_script[0-9]*\.yaml" $HTML_FILE | uniq) )

mv $HTML_FILE /tmp

if [ ! -d out ]; then
  mkdir out
fi
echo $(date) > out/API_VERSION
for spec in ${SPEC_FILES[@]}; do
  qstring="$NEXON_API_ROOT_URL/$spec"
  echo "Spec: $spec | Url: $qstring"
  wget $qstring
  
  grep 'name: User' $spec \
    && mv $spec "out/user.openapi.yaml" \
    &&  echo "user: ${spec}" >> out/API_VERSION \
    && continue
  grep 'name: Recommendation' $spec \
    && mv $spec "out/recommendation.openapi.yaml" \
    && echo "recommendation: ${spec}" >> out/API_VERSION \
    && continue
  grep 'name: Meta' $spec \
    && mv $spec "out/metadata.openapi.yaml" \
    && echo "meta: ${spec}" >> out/API_VERSION \
    && continue
done

dl_specs=($(ls ./out/*openapi.yaml))
for spec in ${dl_specs[@]}; do
  sfn=$(echo $spec | sed 's/.*out\///')
  echo "Diff $spec"
  diff out/$sfn spec/$sfn
done