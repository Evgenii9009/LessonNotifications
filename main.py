import requests
import telegram
import time
import os


def process_attempt(attempt):
    status = 'Работа не принята'
    if attempt['is_negative'] != True:
        status = 'Ваша работа принята!'
    name = attempt['lesson_title']
    url = attempt['lesson_url']
    return status, name, url

def main():
    timestamp = 0
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(tg_token)
    chat_id = 474074848
    while True:
        try:
            url = 'https://dvmn.org/api/long_polling/'
            headers = {'Authorization': 'Token 2e8b8a13209b8dbc3be00a372efb1ae33d67b4fa'}
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