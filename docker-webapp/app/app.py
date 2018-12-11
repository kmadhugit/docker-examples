from flask import Flask, request, render_template

app = Flask(__name__)
cache = {}

def render_page(key,value):
	return render_template('index.html', key=key, cache_value=value)

def set(key,value):
    cache[key] = value

def get(key):
    return cache.get(key,'NA')

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
    app.run(host='0.0.0.0')

