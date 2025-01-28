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
        # Primește datele JSON din cererea POST
        data = request.get_json()
        
        # Obține mesajul și numele utilizatorului
        user_message = data.get("message")
        user_name = data.get("user")

        # Verifică dacă 'message' și 'user' sunt prezente
        if not user_message or not user_name:
            return jsonify({"error": "Missing 'message' or 'user' field"}), 400

        # Trimiterea mesajului către OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        
        # Obține răspunsul de la OpenAI
        reply = response.choices[0].text.strip()

        # Răspunde la cerere cu mesajul generat
        return jsonify({"response": reply})

    except Exception as e:
        # În caz de eroare, returnează un mesaj de debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


