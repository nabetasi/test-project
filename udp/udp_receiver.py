#!/usr/bin/env python

import sys
from socket import socket, AF_INET, SOCK_DGRAM

HOST = ''   
PORT = 10000


def main(args):
    print("udp main")
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((HOST, PORT))
    while True:
        msg, address = s.recvfrom(8192)
        print('message : ' + str(msg) + ', address : ' + str(address))

    s.close()

if __name__ == '__main__':
    main(sys.argv)
    print("end!")
