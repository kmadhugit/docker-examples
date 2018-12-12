import requests

hostname = 'localhost'
port     = 3000
getURL = f'http://{hostname}:{port}/get'
setURL = f'http://{hostname}:{port}/set'

def get(key):
    payload = {}
    payload['key'] = key
    r = requests.post(url=getURL, json=payload)
    data = r.json()
    print(r.url,type(r),type(data),data)
    return data

def set(key,value):
    payload = {}
    payload['key']   = key
    payload['value'] = value
    r = requests.post(url=setURL, json=payload)
    data = r.json()
    print(r.url,type(r),type(data),data)
    return data




set('name','madhu')
get('name')
