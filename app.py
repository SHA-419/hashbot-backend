from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

import os

app = Flask(__name__)
CORS(app)

# Configure Gemini API key from environment variable
genai.configure(api_key=os.getenv("AIzaSyDr2stfQevfP_yAe43YQKVVun63G066Mds"))
model = genai.GenerativeModel("models/gemini-2.0-flash-lite")
chat_session = model.start_chat(history=[])

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get("message", "")
    try:
        response = chat_session.send_message(message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
