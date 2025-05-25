from flask import Flask, request, jsonify
import os
import subprocess
import ast
import ipaddress

app = Flask(__name__)

# Securely load password from environment
PASSWORD = os.environ.get("APP_PASSWORD", "defaultpassword")


@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    if not name.isalnum():
        return jsonify({"error": "Invalid name"}), 400
    return f"Hello, {name}!"


# Safe ping endpoint with input validation and no shell use
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    try:
        ipaddress.ip_address(ip)  # Validates IPv4 or IPv6
        result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f"Invalid IP or Error: {e}", 400


# Safe calculate endpoint using literal_eval instead of eval()
@app.route('/calculate')
def calculate():
    expression = request.args.get('expr')
    try:
        result = ast.literal_eval(expression)
        return str(result)
    except Exception as e:
        return f"Invalid expression: {e}", 400


# Restrict server to localhost only
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
