#!/usr/bin/env bash
set -e

# Активируем виртуальное окружение (если оно в .venv)
source .venv/bin/activate

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

make install