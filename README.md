# PDFer

### Описание

**PDFer** - это веб приложение для уменьшения размера .pdf файлов, созданное на основе фреймворка _Django_ с использованием библиотек _PyPDF2_ и _pdf2image_.

## Установка

**Системные требования:**
Установленные приложения Docker Engine и Docker Compose

---

Для установки приложения необходимо выполнить следующие действия:

1. Клонировать репозиторий на устройство, выполнив команду:
   `$ git clone git@github.com:Mahallis/PDFer.git`

2. Создать файл окружения `.env` в директории `./app` по образцу файла `.env.example`
3. Создать и запустить контейнер выполнив команду в директории с файлом compose.yaml из репозитория:
   `$ docker compose up -d`
