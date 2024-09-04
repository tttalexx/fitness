import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from backend.auth import auth_bp
from backend.views import main_bp
from backend.models import db
from flask import Flask

app = Flask(__name__)
app.config.from_object('configuration.settings')

# Подключаем маршруты из auth.py и views.py
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
