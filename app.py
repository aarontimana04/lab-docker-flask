from flask import Flask, jsonify
import socket
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Flask Docker App</title>
    </head>
    <body>
        <h1>🐳 Flask Docker App</h1>
        <p>¡Aplicación Flask ejecutándose en Docker!</p>

        <p>
            <a href="/api/health">Verificar estado de la API</a>
        </p>

        <p>
            <a href="/api/info">Información del contenedor</a>
        </p>
    </body>
    </html>
    """


@app.route("/api/health")
def health():
    return jsonify({
        "message": "Flask app funcionando correctamente",
        "status": "healthy"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "app": "Flask Docker Demo",
        "hostname": socket.gethostname(),
        "python_version": sys.version,
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
