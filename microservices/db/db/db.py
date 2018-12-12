from flask import Flask, request, jsonify
import os

dbapp = Flask(__name__)
cache = {}
hostname = '0.0.0.0'
port     = os.getenv('DBPORT', 4000)

def set(key,value):
    cache[key] = value
    return jsonify('done')

def get(key):
    return jsonify(cache.get(key,'NA'))

@dbapp.route('/get', methods=['POST'])
def doget():
    data = request.json
    return get(data['key'])

@dbapp.route('/set', methods=['POST'])
def doset():
    data = request.json
    return set(data['key'],data['value'])

if __name__ == '__main__':
    dbapp.run(host=hostname,port=port)

