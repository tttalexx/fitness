import requests

def send_sms(phone_number, message):
    url = "https://api.turbosms.ua/message/send.json"
    api_key = "YOUR_TURBOSMS_API_KEY"  # Замените на ваш API-ключ
    
    payload = {
        "recipients": [phone_number],
        "text": message,
        "sender": "YourSenderName"  # Замените на имя отправителя, зарегистрированное в TurboSMS
    }
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return True
    else:
        print(f"Error sending SMS: {response.text}")
        return False
