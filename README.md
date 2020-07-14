# Readme

Using python 3.8


1. Create .env and .flaskenv in /app dir

    .env

    ``` console
    SECRET_KEY='something_very_secret'
    ```

    .flaskenv

    ``` console
    FLASK_APP=app.py
    FLASK_ENV=development
    POSTGRES_DB=db_name
    POSTGRES_USER=db_user
    POSTGRES_PASSWORD=changeme
    POSTGRES_HOST=db
    LANG='ru_RU.UTF-8'
    LC_ALL='ru_RU.UTF-8'
    LC_CTYPE='ru_RU.UTF-8'
    ```

    .dbenv

    ``` console
    POSTGRES_DB=db_name
    POSTGRES_USER=db_user
    POSTGRES_PASSWORD=changeme
    ```

2. For running use

    ``` console
    docker-compose build
    docker-compose up
    ```

If database initializet db_exist.flag will be created

## Linter
  
1.  For use linter run container end enter:

    ``` console
    docker-compose exec user-service /linter.sh
    ```

2.  Or (if container not running)

    ``` console
    docker-compose run user-service /linter.sh
    ```


