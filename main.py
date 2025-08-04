from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# تابع پاسخ به پیام‌ها
def handle_message(chat_id, text):
    if "سلام" in text:
        response = "سلام! به ربات مشاور کنکور خوش اومدی."
    else:
        response = "پیامت دریافت شد! منتظر پاسخ من باش :)"

    requests.post(API_URL, json={
        "chat_id": chat_id,
        "text": response
    })

# دریافت پیام‌ها از Webhook
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        handle_message(chat_id, text)

    return 'ok'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)


