#!/usr/bin/env bash

ROOT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )/.."

if [[ -z "$CI" ]]; then
    source $ROOT_PATH/scripts/start_venv.sh
fi

cd $ROOT_PATH

export PYTHONPATH=$PYTHONPATH:$ROOT_PATH/tests:$ROOT_PATH/ghastcoiler

cd tests

pytest