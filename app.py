from flask import Flask, request, jsonify
import os
import openai
from dotenv import load_dotenv

# Încarcă variabilele de mediu din fișierul .env
load_dotenv()

# Configurează cheia API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Obține datele din cererea JSON
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Extrage mesajul și numele utilizatorului
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
        
        # Extrage răspunsul
        reply = response.choices[0].text.strip()

        # Răspunsul la întrebarea utilizatorului
        return jsonify({"response": reply})

    except Exception as e:
        # Capturarea erorilor și returnarea mesajului de eroare
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Se pornește serverul Flask
    app.run(debug=True, host="0.0.0.0", port=5001)



