import socket
import IPy as ipy
import requests


def checkIP(ip):
    try:
        ipy.IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)



def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.25)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open.')

    except:
        print('[-] Port ' + str(port) + ' is Closed')


port = range(0, 1000)
IPADDRESS = input("$ Enter Target to Scan: ")
converted_ip = checkIP(IPADDRESS)

for i in port:
    port_scan(converted_ip, port[i])
