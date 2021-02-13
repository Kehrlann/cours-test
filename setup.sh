#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

git submodule update --init
rm reveal.js/index.html
ln -s "$SCRIPT_DIR"/index.html "$SCRIPT_DIR"/reveal.js/index.html
ln -s "$SCRIPT_DIR"/images "$SCRIPT_DIR"/reveal.js/images

pushd reveal.js
  npm i
popd
