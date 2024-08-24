// script.js
function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;

    if (userInput.trim() === '') return;

    const chatbox = document.getElementById('chatbox');
    const userMessage = document.createElement('div');
    userMessage.textContent = userInput;
    userMessage.className = 'user-message';
    chatbox.appendChild(userMessage);

    // Send message to the backend
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.textContent = data.response;
        botMessage.className = 'bot-message';
        chatbox.appendChild(botMessage);
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    document.getElementById('user-input').value = '';
}
