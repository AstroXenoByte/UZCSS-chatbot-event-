from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Handle AJAX request from frontend
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    
    # Define Brainshop API URL and parameters
    api_url = 'http://api.brainshop.ai/get'
    api_key = 'WPEmqQkMNSlTntyV'
    bid = '168976'
    
    # You can use a static UID or generate unique ones per user session
    uid = 'unique_user_id'  # Consider changing this if handling multiple users

    # Construct API request
    response = requests.get(api_url, params={
        'bid': bid,
        'key': api_key,
        'uid': uid,
        'msg': user_message
    })
    
    # Extract response from Brainshop API
    data = response.json()
    bot_message = data.get('cnt', 'Sorry, I did not understand that.')
    
    # Return the response to the frontend
    return jsonify({'message': bot_message})

if __name__ == '__main__':
    app.run(debug=True)

