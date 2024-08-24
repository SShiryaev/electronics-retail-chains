# electronics-retail-chains
## Онлайн платформа-торговой сети электроники
## Инструменты
- Python 3.12
- Django 5.1
- DRF 3.15.2
- PostgreSQL 10+

### Запуск

1. Войдите в корневую папку:

   ```shell
   cd ./test_SP_sertification/
   ```

2. Создайте файл ".env" с вашими переменными окружения по примеру файла '.env.sample':

   ```shell
   cp .env.sample .env
   ```

3. Создайте и активируйте виртуальное окружение poetry:

   ```shell
   poetry init
   poetry shell
   poetry install
   ```

4. Примените миграции:

   ```shell
   python manage.py migrate
   ```

5. Запустите проект:

   ```shell
   python manage.py runserver
   ```
6. Создайте супер-пользователя:
   ```shell
   python manage.py csu
   ```

7. Войдите в админ-панель:

- логин и пароль нужно взять из скрипта users/management/commands/csu.py

8. Использование API:

- Для работы с объектами звеньев сети: [http://127.0.0.1:8000/retail_chains](http://127.0.0.1:8000)
- Для работы с объектами продуктов: [http://127.0.0.1:8000/products](http://127.0.0.1:8000)