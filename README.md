[![Linter check](https://github.com/ReYaNOW/avito-tech-test-task/actions/workflows/pyci.yml/badge.svg)](https://github.com/ReYaNOW/avito-tech-test-task/actions/workflows/pyci.yml)

## Описание
Тестовое задание для avito-tech

Микросервис для сбора статистики по откликам и просмотрам. 
Сервис взаимодействует с клиентом при помощи REST API.  
  
Реализована возможность запуска в Docker.  
Реализована валидация входных данных.

Стек: Python3.11, FastApi, SqlAlchemy, Alembic, Asyncpg, Docker

## Документация
Открыть документацию можно по [ссылке](https://test-task-avito-tech.onrender.com/docs)  
Там же можно поделать запросы к сервису

# Использование


 - Открыть задеплоенный [тестовый вариант](https://avito-tech-test-task.onrender.com)
 - [Развернуть сервис с Docker](#Как-развернуть-сервис-с-Docker)  
 - [Развернуть сервис без Docker](#Как-развернуть-сервис-без-Docker)

![App preview](https://github.com/ReYaNOW/ReYaNOW/blob/main/Images/stats_preview_img.png?raw=true)

## Как развернуть сервис с Docker
1. Склонировать репозиторий

```
git clone https://github.com/ReYaNOW/avito-tech-test-task.git
```

2. Переименовать .env.example в .env  
   [Опционально] указать другую database url для использования своей БД  
  
```
mv .env.example .env
```

3. Установить зависимости и применить миграции к БД
  
```
make compose-setup
```

4. Запустить локальный сервер и открыть http://127.0.0.1:8080
  
```
make compose-start
```


## Как развернуть сервис без Docker
Для этого необходим [Poetry](https://python-poetry.org/docs/#installing-with-pipx)  
  
1. Склонировать репозиторий

```
git clone https://github.com/ReYaNOW/avito-tech-test-task.git
```

2. При запуске без Docker необходимо использовать свою БД PostgreSQL, для этого
   необходимо составить database url  
   Ниже представлен формат такой ссылки  

```
postgresql+asyncpg://[user][:password]@[hostname][:port][/dbname]
```

3. Переименовать .env.example в .env  
   Указать database url в этот файл  
  
```
mv .env.example .env
```

4. Установить зависимости и применить миграции к БД
  
```
make install
```

5. Запустить локальный сервер и открыть http://127.0.0.1:8080

```
make start
```
