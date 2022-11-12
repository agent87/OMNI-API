import requests



def send_sms(sms,number='+250787570975'):
    token = None
    headers = {'Authorization': 'Bearer ' + token}
    data = {'to' : number, 'text' : sms, 'sender' : 'OMNI'}

    url = 'https://api.pindo.io/v1/sms/'
    response = requests.post(url, json=data, headers=headers)
