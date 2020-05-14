#!/usr/bin/env bash
set -e

ROOT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )/.."

source $ROOT_PATH/scripts/start_venv.sh

cd $ROOT_PATH

export PYTHONPATH=$PYTHONPATH:$ROOT_PATH/tests:$ROOT_PATH/ghastcoiler

cd tests

pytest