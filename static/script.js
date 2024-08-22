document.getElementById('user-input').addEventListener('keydown', checkEnter);

function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addMessage(userInput, "user-message");
        document.getElementById("user-input").value = "";

        // Simulate bot response
        setTimeout(function() {
            var botResponse = "I'm here to help!";
            addMessage(botResponse, "bot-message");
        }, 1000);
    }
}

function addMessage(message, className) {
    var chatbox = document.getElementById("chatbox");
    var messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.textContent = message;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function checkEnter(event) {
    if (event.key === "Enter") {
        if (event.shiftKey) {
            // For Shift+Enter: insert a new line
            event.preventDefault();
            const input = event.target;
            const start = input.selectionStart;
            const end = input.selectionEnd;
            input.value = input.value.substring(0, start) + "\n" + input.value.substring(end);
            input.selectionStart = input.selectionEnd = start + 1;
        } else {
            // For Enter without Shift: send message
            event.preventDefault();
            sendMessage();
        }
    }
}