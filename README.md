🚀 Task Manager API
Простой и эффективный менеджер задач с полноценным REST API, построенный на современном стеке технологий.

https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white

✨ Особенности
🚀 Высокая производительность на базе FastAPI

✅ Полное CRUD для управления задачами

🎯 Три статуса задач: создано, в работе, завершено

📊 Автогенерируемая документация Swagger/ReDoc

🧪 100% покрытие тестами (unit + integration)

🐳 Docker-контейнеризация

🔒 Валидация данных через Pydantic

📝 Логирование и обработка ошибок

🛠 Технологический стек
Компонент	Технология	Версия
Backend	FastAPI	0.104+
Тесты	pytest	7.4+
База данных	SQLite	3.x
Контейнеризация	Docker	20.10+
Валидация	Pydantic	2.4+
ORM	SQLAlchemy	2.0+
📦 Быстрый старт
Вариант 1: Запуск через Docker (рекомендуется)
bash
# Клонирование репозитория
git clone https://github.com/MaksLevchenko/task-manager.git
cd task-manager

# Запуск приложения
docker-compose up -d

# Проверка статуса
docker-compose ps

# Просмотр логов
docker-compose logs -f web
Вариант 2: Локальная установка
bash
# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate    # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Запуск тестов
pytest tests/ -v
🌐 Доступ к API
После запуска приложение доступно по адресам:

API Документация (Swagger): http://localhost:8000/docs

Альтернативная документация (ReDoc): http://localhost:8000/redoc

Health Check: http://localhost:8000/

📋 API Endpoints
🎯 Работа с задачами
Метод	Endpoint	Описание	Статусы
GET	/tasks/	Получить список задач	200 OK
POST	/tasks/	Создать новую задачу	201 Created
GET	/tasks/{id}	Получить задачу по ID	200 OK, 404 Not Found
PUT	/tasks/{id}	Обновить задачу	200 OK, 404 Not Found
DELETE	/tasks/{id}	Удалить задачу	200 OK, 404 Not Found
📊 Модель задачи
json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Важная задача",
  "description": "Описание важной задачи",
  "status": "created"
}
Статусы задач:

created - создана

in_progress - в работе

completed - завершена

🧪 Тестирование
Проект включает комплексную тестовую систему:

Запуск тестов
bash
# Все тесты
docker-compose run test

# Только unit-тесты
pytest tests/test_tasks.py -v

# Только integration-тесты
pytest tests/test_main.py -v

# С покрытием кода
pytest --cov=app tests/

# С генерацией HTML отчета
pytest --cov=app --cov-report=html tests/
Структура тестов
tests/test_tasks.py - Unit тесты бизнес-логики

tests/test_main.py - Integration тесты API

tests/conftest.py - Конфигурация тестового окружения

Покрытие тестами:

✅ CRUD операции

✅ Валидация данных

✅ Обработка ошибок

✅ HTTP статус коды

✅ Работа с базой данных

🐳 Docker конфигурация
Сервисы
web - Основное приложение на FastAPI

test - Сервис для запуска тестов

Переменные окружения
env
DATABASE_URL=sqlite:///./test.db
PYTHONPATH=/app
📁 Структура проекта
text
task-manager/
├── app/                    # Исходный код приложения
│   ├── __init__.py        # Пакет приложения
│   ├── main.py            # Точка входа FastAPI
│   ├── models.py          # SQLAlchemy модели
│   ├── schemas.py         # Pydantic схемы
│   ├── crud.py           # Бизнес-логика (CRUD)
│   └── database.py       # Конфигурация БД
├── tests/                 # Тесты
│   ├── __init__.py
│   ├── conftest.py       # Конфигурация pytest
│   ├── test_tasks.py     # Unit тесты
│   └── test_main.py      # Integration тесты
├── Dockerfile            # Конфигурация Docker
├── docker-compose.yml    # Docker Compose
├── requirements.txt      # Зависимости Python
└── README.md            # Документация
🚀 Примеры использования
Создание задачи
bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Изучить FastAPI",
    "description": "Освоить основы FastAPI и pytest",
    "status": "in_progress"
  }'
Получение списка задач
bash
curl "http://localhost:8000/tasks/"
Обновление задачи
bash
curl -X PUT "http://localhost:8000/tasks/{task_id}" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'


Тесты: 100% покрытие

Зависимости: Минимальный набор

🤝 Contributing
Форкните репозиторий

Создайте feature ветку (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте ветку (git push origin feature/amazing-feature)

Откройте Pull Request

📄 Лицензия
Этот проект распространяется под лицензией MIT. См. файл LICENSE для подробностей.

🆘 Поддержка
Если у вас возникли вопросы:

Проверьте документацию в Swagger

Посмотрите открытые issues

Создайте новый issue с описанием проблемы

⭐ Если проект вам понравился, не забудьте поставить звезду!

Разработано с ❤️ на современном стеке технологий