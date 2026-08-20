import requests

data_to_be_sent = {
    'sl' : '1.2',
    'sw' : '3.2',
    'pl' : '0.2',
    'pw' : '0.1',
}

url = 'http://127.0.0.1:5000/prediction'
response = requests.post(data = data_to_be_sent, url = url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)