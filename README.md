![example workflow](https://github.com/Michelin90/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Cat_charity_fund
## Язык и инструменты:
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastApi](https://img.shields.io/badge/FastAPI-0.78-blue?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-blue?style=for-the-badge&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
![Pydantic](https://img.shields.io/badge/Pydantic-1.9-blue?style=for-the-badge&logo=Pydantic)

## Описание
Фонд собирает пожертвования на различные целевые проекты, связанные с поддержкой кошачьей популяции.
### Проекты
В фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
### Пользователи
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Michelin90/cat_charity_fund.git
cd cat_charity_fund
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Создать в корневой папке файл .env и добавить в него следующие строки:
```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=<строка, на основе которой будет генерироваться токен для пользователя>
```
Выполнить миграции:
```
alembic upgrade head
```
Запустить проект:
```
uvicorn app.main:app --reload
```
После запуска проект будет доступен по адресу: http://127.0.0.1:8000

Документация к API досупна по адресам:

Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
