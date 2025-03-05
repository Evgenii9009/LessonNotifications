import requests
import telegram
import time
import os
import sys


def process_attempt(attempt):
    status = 'Работа не принята'
    if attempt['is_negative'] != True:
        status = 'Ваша работа принята!'
    name = attempt['lesson_title']
    url = attempt['lesson_url']
    return status, name, url

def main():
    timestamp = 0
    url = 'https://dvmn.org/api/long_polling/'
    try:
        tg_token = os.environ['TG_BOT_TOKEN']
        chat_id = os.environ['TG_CHAT_ID']
        token = os.environ['DEVMAN_TOKEN']
        bot = telegram.Bot(tg_token)
        headers = {'Authorization': token}
    except KeyError:
        print('Укажите значения переменных окружения!')
        sys.exit()
    while True:
        try:
            if timestamp:
                payload = {'timestamp': timestamp}
                response = requests.get(url, headers=headers, params=payload)
                response.raise_for_status()
            else:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
            result = response.json()
            if result['status'] != 'timeout':
                timestamp = result['new_attempts'][0]['timestamp']
                for attempt in result['new_attempts']:
                    status, name, lesson_url = process_attempt(attempt)
                    bot.send_message(chat_id=chat_id, text=f'Урок: {name}\n Результат проверки: {status}\n Ссылка на занятие: {lesson_url}')

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            print('Соединение потеряно...')
            time.sleep(30)
            continue


if __name__ == '__main__':
    main()