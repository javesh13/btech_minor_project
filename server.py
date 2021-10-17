#!/usr/bin/python

#Python server to recieve media

import socket , func_dict as fd, decode_codes as dc

from datetime import datetime as dt
from threading import Thread
HOST = '0.0.0.0'
PORT = 12345

print("Waiting for client on "+str(HOST)+":"+str(PORT))

ADDR = (HOST,PORT)
BUFFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv.bind(ADDR)
serv.listen(100)

print 'listening ...'

(conn, (ip ,port ))= serv.accept()
print 'client connected ... ' + str(ip)+":"+str(port)

data="a"
while True:
    (con, (ip, port)) = serv.accept()
    print("Client connected ...." + str(ip) + ":" + str(port))
    t1 = Thread(target = proc_client, args = ((con,)))
    t1.start()
    
def proc_client(con):
    data = "a"
    while len(data):
        data = con.recv(BUFFSIZE)
        print("Data is: " + data)
        t1 = Thread(target = fd.process_data, args = ((data,)))
        t1.start()


