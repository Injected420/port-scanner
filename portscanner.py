import sys
import socket
import threading
import IPy as ipy
import requests
import datetime

START = datetime.datetime.now()

def checkIP(ip):
    try:
        ipy.IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.10)
        sock.connect((ipaddress, port))
        print('[+] Port **%d** OPEN' % port)
    except KeyboardInterrupt:
        print("[!]Program exited by user.")
        sys.exit(1)
    except:
        print('[-] Port %d CLOSED' % port)

IPADDRESS = input("$ Enter Target to Scan: ")
port = (input("$ Enter the last port number you want to scan: \r\nOr Enter 'C' if you want to scan the most common ports (1-1024): "))
if port == "C" or "c":
    port = range(1024)
else:
    port = range(port)
print(socket.gethostbyname(IPADDRESS), "started at", START)
converted_ip = checkIP(IPADDRESS)
def do_scan():
        for i in port:
            port_scan(converted_ip, port[i])
do_scan()
