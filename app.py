from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    
    return jsonify(response["choices"][0]["message"])
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'הצ\'אטבוט מחובר ועובד ✅'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
