# 📦 Stocks & Products API

REST API для управления продуктами и складами, разработанный на **Django REST Framework**.

## 🚀 Функционал

- **Полный CRUD** для продуктов и складов (создание, чтение, обновление, удаление).
- **Связь "Многие ко многим"** через промежуточную модель `StockProduct` (у одного продукта может быть разная цена и количество на разных складах).
- **Кастомные методы сериализатора**: переопределены `create` и `update` для корректной обработки вложенного списка продуктов при создании/обновлении склада (используется `update_or_create`).
- **Поиск**:
  - Продукты ищутся по названию и описанию (`?search=...`).
  - Склады ищутся по наличию продукта (по названию или описанию продукта).
- **Пагинация**: списки выводятся по 10 элементов на страницу (настроено глобально).

## 🛠 Технологии

- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL
- Swagger / OpenAPI (для документации)
## ⚙️ Установка и запуск

1. **Клонировать репозиторий:**
   ```bash
   git clone https://github.com/askoline-sketch/stocks-products-api.git
   cd stocks-products-api
2. **Создать и активировать виртуальное окружение:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Для Mac/Linux
3. **Установить зависимости:**

   ```bash
   pip install -r requirements.txt
4. **Настроить базу данных:**

Создайте базу данных PostgreSQL: createdb netology_stocks_products

Укажите свои данные для подключения в файле stocks_products/settings.py (блок DATABASES).

5. **Применить миграции:**

   ```bash
   python manage.py migrate
6. **Запустить сервер:**

   ```bash
   python manage.py runserver
### 📡 Основные эндпоинты
GET /api/v1/products/ — список продуктов (с пагинацией).

GET /api/v1/products/?search=помидор — поиск продуктов.

POST /api/v1/products/ — создание продукта.

GET /api/v1/stocks/ — список складов с вложенным списком продуктов.

GET /api/v1/stocks/?search=огурец — поиск складов, где есть продукт.

POST /api/v1/stocks/ — создание склада с продуктами.

### 👨‍💻 Автор
Пузиков Геннадий (askoline-sketch)

GitHub

Telegram
