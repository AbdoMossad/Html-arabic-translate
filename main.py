from flask import Flask
from app.routes import translate_bp

app = Flask(__name__)
app.register_blueprint(translate_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
