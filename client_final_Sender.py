#!/usr/bin/python

#HARDCODING DATA STRING TO SEND

import socket,sys

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])

print("Connecting to "+str(HOST)+":"+ str(PORT))

ADDR = (HOST,PORT)
BUFSIZE = 4096

roll_num = raw_input("Enter your Roll Number : ")
group = raw_input("Enter your Group : ")
name=raw_input("Enter you Name : ")
email = raw_input("Enter your Email : ")
number=raw_input("Enter you Mobile Number : ")

registeration_request = "281001"+roll_num+name+","+email+","+group+","+number+"29"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print ("Registering on server......")

client.send(registeration_request)

while True:

	
	todo = raw_input("Press 1 to chat \n")
  	
  	if (str(todo) == "1"):
 		roll=raw_input("Enter the roll number of ther person you want to chat with")
        	message=raw_input("Wnter the message you want to send")
        	message_request = "283001"+roll_num+roll+","+message+",29"
   		client.send(message_request)
   	

client.close()
