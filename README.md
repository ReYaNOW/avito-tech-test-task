### Описание
Тестовое задание для avito-tech

Стек: Python3.11, FastApi, SqlAlchemy, Alembic, Asyncpg, Docker

### Установка

# Использование


 - Открыть задеплоенный на render.com [тестовый вариант](https://task-manager-hexlet.onrender.com/)
 - [Развернуть приложение с Docker](#Как-развернуть-приложение-с-Docker)  
 - [Развернуть приложение без Docker](#Как-развернуть-приложение-без-Docker)

![ВСТАВИТЬ КАРТИНКУ](https://github.com/ReYaNOW/ReYaNOW/blob/main/task_manager_preview.pnggg?raw=true)

## Как развернуть приложение с Docker
1. Склонировать репозиторий

```
git clone https://github.com/ReYaNOW/avito-tech-test-task.git
```

2. Переименовать .env.example в .env.  
   [Опционально] указать другую database url для использования своей БД.  
  
```
mv .env.example .env
```

3. Установить зависимости и применить миграции к БД
  
```
make compose-setup
```

4. Запустить при помощи ``make compose-start``


## Как развернуть приложение без Docker
1. Склонировать репозиторий

```
git clone https://github.com/ReYaNOW/avito-tech-test-task.git
```

2. При запуске без Docker необходимо использовать свою БД PostgreSQL, для этого
   необходимо составить database url.
   Ниже представлен формат такой ссылки.

```
postgresql+asyncpg://[user][:password]@[hostname][:port][/dbname]
```

3. Переименовать .env.example в .env.  
   Указать database url в этот файл.

4. Установить зависимости и применить миграции к БД
  
```
make install
```

5. Запустить локальный сервер для разработки

```
make start
```
