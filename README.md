# Уведомления о проверке работ на [Devman](https://dvmn.org/)

Код предназначен для уведомления учеников о проверке их работ с помощью телеграм-бота

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Запуск

Для работы вам потребуются следующие переменные окружения:
 - TG_BOT_TOKEN - Токен вашего бота, его нужно получить при создании бота через [BotFather](https://t.me/BotFather)
 - TG_CHAT_ID - ID вашего чата с ботом, можно получить через [userinfobot](https://telegram.me/userinfobot)
 - DEVMAN_TOKEN - Токен для работы с API Devman

Все эти переменные должны быть указаны в .env файле в корне проекта

Запуск осуществляется командой 

```
python3 main.py
```
### Пример работы

![Screenshot from 2025-03-05 18-06-21](https://github.com/user-attachments/assets/90e1a95f-433a-475d-b0d5-6d1194cf2cc5)

