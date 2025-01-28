from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Setează cheia API OpenAI (înlocuiește cu cheia ta)
openai.api_key = "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"

@app.route("/", methods=["POST"])
def handle_request():
    data = request.json
    user_message = data.get("message", "")  # Mesajul trimis de utilizator

    # Creează răspuns cu OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Poți folosi și "gpt-4" dacă ai acces
            prompt=user_message,
            max_tokens=100
        )
        ai_response = response.choices[0].text.strip()
    except Exception as e:
        ai_response = "Îmi pare rău, nu am reușit să procesez cererea."

    # Trimite răspunsul înapoi
    return jsonify(ai_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
