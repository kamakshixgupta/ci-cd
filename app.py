from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 DevOps CI/CD Demo</h1>
    <h2>Deployment Successful!</h2>

    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Current Time:</b> {datetime.now()}</p>

    <hr>

    <h3>Pipeline:</h3>

    <p>
    GitHub → CI/CD Pipeline → Private EC2
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)