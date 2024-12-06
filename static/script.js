// Connect to the WebSocket server
const socket = io();

// Send a message when the user clicks the Send button
document.getElementById('send-button').addEventListener('click', () => {
    const message = document.getElementById('message-input').value;
    if (message.trim()) {
        socket.send(message);
        document.getElementById('message-input').value = '';
    }
});

// Listen for messages from the server
socket.on('message', (message) => {
    const messagesDiv = document.getElementById('messages');
    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    messagesDiv.appendChild(newMessage);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
});
