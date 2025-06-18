#!/usr/bin/env bash
set -e

# Скачиваем и устанавливаем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"

# Активируем виртуальное окружение
source .venv/bin/activate

make install
make migrate
