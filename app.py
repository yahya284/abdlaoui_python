from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Route to serve the chat page
@app.route('/')
def chat():
    return render_template('chat.html')

# Handle incoming messages
@socketio.on('message')
def handle_message(message):
    print(f"Message received: {message}")
    send(message, broadcast=True)  # Broadcast the message to all connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
