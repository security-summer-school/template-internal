import sys
import requests

PORT = 8001

if len(sys.argv) > 1 and sys.argv[1] == 'local':
    HOST = '127.0.0.1'
else:
    HOST = '141.85.224.103'

res = requests.get('http://%s:%d' % (HOST, PORT))
