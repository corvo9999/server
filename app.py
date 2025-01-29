from flask import Flask, request, jsonify
import openai
import os

# Configurează cheia API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Serverul funcționează!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    user_name = data.get("user")

    if not user_message or not user_name:
        return jsonify({"error": "Missing message or user"}), 400

    # Trimiterea mesajului către OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    
    reply = response.choices[0].text.strip()
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)




