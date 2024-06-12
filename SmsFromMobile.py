import requests
api_key="7f3327a40519291bd36576593bc4417bedbc9542"
device_id="00000000-0000-0000-9954-493415ef70b1"

def send_sms(api_key,device_id,number,message):
    message = {
        "secret": api_key,
        "mode": "devices",
        "device": device_id,
        "sim": 1,
        "priority": 1,
        "phone": number,
        "message": message
    }

    r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)  
    # do something with response object
    result = r.json()
    return result
number=input("Enter the number of the person you wanna send your sms too (along with country code):")
text=input("Enter the message you want to send:")
print(send_sms(api_key,device_id,number,text))
