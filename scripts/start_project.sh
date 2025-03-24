#!/usr/bin/env bash
set -e

export ENVIRONMENT=local
export PYTHONDONTWRITEBYTECODE=1

# Путь к основному .env файлу
MAIN_ENV=.src.env
TEMPLATE_ENV=.env.example

# Создаем .env из примера если отсутствует
if [[ ! -f ${MAIN_ENV} ]]; then
    if [[ -f ${TEMPLATE_ENV} ]]; then
        cp "${TEMPLATE_ENV}" "${MAIN_ENV}"
        echo "✅ Создан ${MAIN_ENV} из шаблона"
    else
        echo "❌ Отсутствует ${MAIN_ENV} и шаблон ${TEMPLATE_ENV}"
        exit 1
    fi
fi

# Запуск контейнеров
echo "🚀 Запуск Docker-сервисов..."
docker-compose up --build --detach

echo -e "\n⏳ Ожидание инициализации БД..."
docker-compose exec db bash -c '
    until pg_isready -U $POSTGRES_USER -d $POSTGRES_DB; do
        echo "Ждем PostgreSQL..."
        sleep 2
    done'

echo -e "\n🛠 Выполнение миграций..."
docker-compose exec app alembic upgrade head

echo -e "\n🔍 Проверка сервисов:"
docker-compose exec app bash -c '
    echo "Запуск FastAPI...";
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload &

    echo "Запуск Telegram бота...";
    python src/telegram/bot.py &

    wait'

echo -e "\n✅ Все компоненты запущены!\nДоступные сервисы:"
echo "• FastAPI: http://localhost:8000/docs"
echo "• PostgreSQL: localhost:5432"