from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Mensagem recebida: ' + message)
    socketio.emit('message', message)  # Envia a mensagem para todos os clientes conectados

if __name__ == '__main__':
  socketio.run(app, debug=True)