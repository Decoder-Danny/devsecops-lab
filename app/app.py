from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True)
    return result.stdout.decode()

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)