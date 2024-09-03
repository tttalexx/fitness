import requests

def send_sms(phone_number, message):
    url = "https://api.turbosms.ua/message/send.json"
    api_key = "8b21cdea4d152f36e9ace51467da09048f871529" 
    
    payload = {
        "recipients": [phone_number],
        "text": message,
        "sender": "MaryCoach"
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
