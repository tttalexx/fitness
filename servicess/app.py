from flask import Flask, request, jsonify
from services.sms_service import send_sms

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    phone_number = request.json.get('phone')
    if send_sms(phone_number, "Your verification code is 123456"):
        return jsonify({"status": "SMS sent"}), 200
    else:
        return jsonify({"status": "Error"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
