from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8936034857:AAHjkk8t7-p-4DvPWtjPNGpHAfbnblm3_Vs"
CHAT_ID = "5936405189"

@app.route('/')
def home():
    return "BOT RUNNING"

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    message = data['message']

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        telegram_url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return "OK"

app.run(host='0.0.0.0', port=5000)
