from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# In-memory storage for conversation (optional for demo purposes)
conversation = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    # Simple response logic (you can expand this with actual chatbot logic)
    bot_response = "You said: " + user_message
    
    # Store conversation (optional)
    conversation.append({"user": user_message, "bot": bot_response})

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
