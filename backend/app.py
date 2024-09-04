from flask import Flask
import os
from backend.auth import auth_bp
from backend.views import main_bp

# Указываем путь к папке с шаблонами, которая находится в frontend/templates
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'frontend/templates'))
app.config.from_object('config.settings')

# Подключаем маршруты из auth.py и views.py
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
