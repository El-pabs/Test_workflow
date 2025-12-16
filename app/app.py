from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Affiche le nom du serveur (Pod) pour prouver que ça tourne
    return f"<h1>Hello depuis AWS EC2 ! test 1</h1><p>Servi par le pod: {socket.gethostname()}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
