from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot Running Successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if "hello" in user_message.lower():
        response = "Hi! How can I help you?"
    else:
        response = "I am an AI chatbot."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)