#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

git submodule update --init

pushd reveal.js
  git fetch
  git checkout -- package.json index.html
  git checkout origin/master
  npm i
popd

rm "$SCRIPT_DIR"/reveal.js/index.html
ln -s "$SCRIPT_DIR"/index.html "$SCRIPT_DIR"/reveal.js/index.html
rm "$SCRIPT_DIR"/reveal.js/images
ln -s "$SCRIPT_DIR"/images "$SCRIPT_DIR"/reveal.js/images

