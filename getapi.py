import json
import requests

print 'hellow-python'

print 'getapi'

url = 'http://localhost:5984/imagelist/'
key = '6a68cff2f67da8389cef0bb0ca000a3b'

result = requests.get(url+key)

print result.text