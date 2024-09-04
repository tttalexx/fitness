from flask import Flask
from auth import auth_bp
from views import main_bp
from backend.auth import auth_bp
from backend.views import main_bp

app = Flask(__name__)
app.config.from_object('backend.configuration')

# Подключаем маршруты из auth.py и views.py
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
