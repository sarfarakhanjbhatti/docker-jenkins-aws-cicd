from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Jenkins AWS CI/CD</title>
    </head>
    <body>
        <h1>Docker + Jenkins + AWS CI/CD</h1>
        <p>Application deployed successfully!</p>
        <p>Built with Docker and deployed through Jenkins.</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    