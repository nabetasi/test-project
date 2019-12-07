#!/usr/bin/env python

import sys

from pythonosc import dispatcher
from pythonosc import osc_server

def print_volume_handler(address, *args):
    print("osc handler")

def main(args):
    osc_ip = "127.0.0.1"
    osc_port = 1337

    print("osc test")

    dispatcher = Dispatcher()
    #dispatcher.map("/filter", print)
    dispatcher.map("/volume", print_volume_handler, "Volume")
    #dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
    server = osc_server.ThreadingOSCUDPServer((osc_ip, osc_port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

if __name__ == '__main__':
    main(sys.argv)
    print("end!")
