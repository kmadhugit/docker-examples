from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)
cache = {}

def render_page(key,value):
	return render_template('index.html', key=key, cache_value=value)


dbhostname = os.getenv('DBHOST', 'dbcontainer')
dbport     = os.getenv('DBPORT', 4000)
myport     = os.getenv('APPPORT',5000)

getURL = f'http://{dbhostname}:{dbport}/get'
setURL = f'http://{dbhostname}:{dbport}/set'

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


@app.route('/', methods=['GET', 'POST'])

#For GET method or POST method refresh action we will render empty page.
def mainpage():

    key = value = ''

    if request.method == 'POST':
        action = request.form['submit']
        if action == 'save':
            set(request.form['key'],request.form['cache_value'])
        elif action == 'load':
           key   = request.form['key']
           value = get(key)
    return render_page(key,value)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=myport)

