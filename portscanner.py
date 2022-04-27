import socket
import threading
import IPy as ipy
import datetime
import sys

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
        print("Port ** %d ** is Open" % port)

    except:
        print("Port %d Closed" % port)


if __name__ == "__main__":

    
    IPADDRESS = input("$ Enter Target to Scan: ")
    port = int(input("$ Enter the last port number you want to scan: "))
    port = range(port)
    print("Scan of", socket.gethostbyname(IPADDRESS), "started at", START)

    converted_ip = checkIP(IPADDRESS)

    def do_scan():
        for i in port:
            port_scan(converted_ip, port[i])

    do_scan()
