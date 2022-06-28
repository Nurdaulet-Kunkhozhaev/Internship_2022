import time

DEST_IP_ADDR = "localhost"
DEST_PORT = 65432
PORT = 65433
BUF_SIZE = 1000
SLEEP_TIME = 3 # In seconds

from socket import socket, AF_INET, SOCK_DGRAM

with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind(("localhost", PORT))

    while True:
        PACKET_DATA = "Some data"
        print("Sending packets <%s>" % PACKET_DATA)
        s.sendto(PACKET_DATA.encode(), (DEST_IP_ADDR, DEST_PORT))
        time.sleep(SLEEP_TIME)
