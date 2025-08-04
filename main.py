from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = 'توکن ربات خودت رو اینجا بذار'

@app.route('/', methods=['GET'])
def index():
    return "ربات فعاله ✅"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # جواب ساده
        response_text = f"پیامت رو گرفتم: {text}"

        # ارسال پیام به تلگرام
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": chat_id,
            "text": response_text
        })

    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)



