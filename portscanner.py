import socket
import threading
import IPy as ipy
import requests
import sys
import datetime


class Color:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


START = datetime.datetime.now()


def checkIP(ip):
    try:
        ipy.IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.10)
        sock.connect((ipaddress, port))
        print(
            f'{Color.GREEN}[+]{Color.RESET} Port: {Color.BOLD}{port}{Color.RESET} is Open.')
    except KeyboardInterrupt:
        print(f"\r\n{Color.RED}[!]{Color.RESET} Program exited by user")
        sys.exit(1)
    except:
        print(
            f'{Color.YELLOW}[-]{Color.RESET} Port: {Color.BOLD}{port}{Color.RESET} is Closed')


def do_scan():
    try:
        IPADDRESS = input(f"{Color.BLUE}${Color.RESET} Enter Target to Scan: ")
        port = int(input(
            f"{Color.BLUE}${Color.RESET} Enter the last port number you want to scan: "))

        converted_ip = checkIP(IPADDRESS)

        for i in range(1, port + 1):
            port_scan(converted_ip, i)
    except KeyboardInterrupt:
        print(f"\n[{Color.MAGENTA}*{Color.RESET}] Scanning Ended by user {Color.BOLD}{Color.CYAN}(Ctrl+c){Color.RESET}. Exiting...\n")
        sys.exit()
    print("[*]Host:", socket.gethostbyname(IPADDRESS), "scan started at", START)


do_scan()
