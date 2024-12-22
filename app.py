from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Event for handling incoming messages from the user
@socketio.on('user_message')
def handle_message(message):
    # Here we can implement AI logic or responses
    # For now, we'll just echo the message for testing
    response = f"AI Mechanic: {message}"
    emit('ai_response', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)
