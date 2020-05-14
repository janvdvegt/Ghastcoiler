#!/usr/bin/env bash
set -e

ROOT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )/.."

python -m venv $ROOT_PATH/.venv || python3 -m venv $ROOT_PATH/.venv
source $ROOT_PATH/.venv/bin/activate
pip install -r $ROOT_PATH/ghastcoiler/requirements.txt || pip3 install -r $ROOT_PATH/ghastcoiler/requirements.txt 
