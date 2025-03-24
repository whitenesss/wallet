# Wallet Management API

Микросервис для управления электронными кошельками с поддержкой транзакций

![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue)
![Python](https://img.shields.io/badge/Python-3.12%2B-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-orange)

## Особенности

- ✅ Создание кошельков с уникальными UUID
- 🔄 Операции пополнения (DEPOSIT) и списания (WITHDRAW)
- 📊 Просмотр баланса и списка всех кошельков
- 🚀 Асинхронная обработка запросов
- 🔒 Оптимистичные блокировки для конкурентных операций
- 🐳 Полная контейнеризация с Docker Compose
- 📝 Автоматическая документация Swagger

## Стек технологий

- **API**: FastAPI
- **База данных**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0
- **Миграции**: Alembic
- **Тестирование**: pytest + AsyncClient
- **Контейнеризация**: Docker + Docker Compose

## Запуск проекта

### Требования

- Docker 20.10+
- Docker Compose 2.20+

### Установка

```bash
git clone https://github.com/whitenesss/wallet.git
cd wallet-app
```

### Запуск
```bash
./scripts/start_project.sh
```
После запуска документация API будет доступна по адресу:
http://localhost:8000/docs

### Структура проекта кратко

```bazaar
wallet_app/
├── docker-compose.yml         # Конфигурация Docker
├── Dockerfile                 # Сборка образа приложения
├── src/                       
│   ├── api/                   # Роутеры и эндпоинты
│   ├── models/                # Модели базы данных
│   ├── schemas/               # Pydantic схемы
│   ├── services/              # Бизнес-логика
│   ├── migrations/            # миграций Alembic
│   └── tests/                 # тесты
├── scripts/                   # скрипт запуска

```
### API Endpoints

```
Создание кошелька
POST /api/v1/wallets/create_wallet

Response:

json
{
  "wallet_id": "550e8400-e29b-41d4-a716-446655440000",
  "balance": "0.00"
}

```

```
Создание кошелька
POST /api/v1/wallets/create_wallet

Response:

json
{
  "wallet_id": "550e8400-e29b-41d4-a716-446655440000",
  "balance": "0.00"
}
```

```
Выполнение операции
POST /api/v1/wallets/{wallet_id}/operation

Request:

json

{
  "operation_type": "DEPOSIT",
  "amount": "100.50"
}
Response:

json

{
  "message": "Operation successful",
  "new_balance": "100.50"
}
```

```
Получение всех кошельков
GET /api/v1/wallets/get_all

Response:

json

[
  {
    "wallet_id": "550e8400-e29b-41d4-a716-446655440000",
    "balance": "100.50"
  }
]
```

### Запуск тестов 
```bash
docker-compose -f docker-compose.test.yml up --build      

```

