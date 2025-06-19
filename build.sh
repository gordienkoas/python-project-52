#!/usr/bin/env bash
set -e

# Устанавливаем uv (если ещё не установлен)
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Добавляем ~/.local/bin в PATH, если там установлен uv
export PATH=$HOME/.local/bin:$PATH

# Активируем виртуальное окружение
source .venv/bin/activate

# Запускаем make install и make migrate
make install
