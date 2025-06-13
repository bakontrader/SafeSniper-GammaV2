from flask import Flask, request
import requests
import datetime

app = Flask(_name_)

TELEGRAM_TOKEN = '7636617234:AAHGDhIEJP9T35w6UYJ2NfdVt5SIJVvs9gg'
CHAT_ID = '1075729672'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f'Telegram error: {e}')

@app.route('/', methods=['GET'])
def home():
    return '🤖 SafeSniper v2.0 сервер запущен!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    signal = data.get('signal', '❓Нет сигнала')
    ticker = data.get('ticker', 'Неизвестный тикер')
    price = data.get('price', 'Цена не указана')

    message = f"""
📈 SafeSniper v2.0 Сигнал
⏰ {now}
📍 Тикер: {ticker}
📊 Сигнал: {signal}
💰 Цена: {price}
"""
    send_telegram_message(message)
    return {'status': 'ok'}

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=10000)
