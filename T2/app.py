from flask import Flask
import socket

app = Flask(__name__)


@app.route('/')
def index():
    return f"Here for the test and I am the container: {socket.gethostname()}"


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5100,
        debug=True
    )
