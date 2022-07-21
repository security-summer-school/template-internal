import sys
import requests

PORT = 8001

if len(sys.argv) == 1:
    print("Please provide at least one argument, \"local\" or \"remote\" depending on where you want to run the solution.")
    print("To run the solution for a different server, you can put sys.argv[1] = IP, sys.argv[2] = PORT.")
    exit(1)

if len(sys.argv) > 1 and sys.argv[1] == 'local':
    HOST = '127.0.0.1'
elif len(sys.argv) > 1 and sys.argv[1] == 'remote':
    HOST = '141.85.224.103'
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

res = requests.get('http://%s:%d' % (HOST, PORT))
