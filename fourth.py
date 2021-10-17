#!/usr/bin/python
import regex as rx
import os
from datetime import datetime as dt

   # Every Method will have their own file , where they will store their data 

   #The Method will be called based on the its codes.

    # MEDIA SENDING IS TO BE SORTED OUT YET BE IT IMAGE/VIDEO/PDF/TXT/AUDIO "

    #Instead of  comma seperated try to use colon seperated
registered_users = []
got_users = False

def decode_1001(con, data):
    #1 time Registeration of user
    #data="28 1001 04414802714 harshit,hkhurana3@gmail.com,9999620964 29"
    actual=data[2:-2]
    code=actual[0:4]
    sender=actual[4:15]
    details=actual[15:]
    name=details.split(",")[0]
    email=details.split(",")[1]	
    group=details.split(",")[2]
    number=details.split(",")[3]
    print(registered_users)
    #branch_dic = {"027":cse, ""...}
    global got_users
    if not got_users:
        try:
            with open("users.txt", "r") as f:
                for line in f.readlines():
                    if(len(line) > 1):
                        registered_users.append(line.rstrip())
            got_users = True
        except:
            with open("users.txt","w") as f:
                f.write("")

    if(sender not in registered_users):
        with open("registeration_1001.txt","a") as f:
            f.write(sender+":"+ group + ":" + name + ":" + email + ":" + number + "\n")
        with open("users.txt", "a") as f:
            f.write(sender + "\n")
        registered_users.append(sender)
        con.send(b"Registered Success Fully")
    else:
        con.send(b"Already Registered")


 
def decode_1002(con, data):

    
    #Dummy Request for keeping connection alive
    #data="28 1002 04414802714 29"
    actual=data[2:-2] 
    code=actual[0:4]
    sender=actual[4:]
    print("App connected\n")

def decode_1003(con, data):


    #Location Sending via IP of client 
    #data= "28100304414802714,192.168.120.10329"

    actual=data[2:-2]
    code=actual[0:4]
    sender=actual.split(",")[0][4:]
    IpOfSender=actual.split(",")[1]

    with open("LocationviaIP_1003.txt","a") as f:
    	f.write("Student : "+sender+"\tIP : "+IpOfSender+"\tTime : "+str(str(dt.now()).split(".")[:-1]) + "\n")

def decode_1004(con, data):
    #checking for messages for client

    roll_number= data[6:17]
    tosend_msg = []
    with open(roll_number+".txt", "r") as f:
        for line in f.readline():
            sender  = line.split(":")[0]
            msg = line.split(":")[1]
            tosend.append(sender+":"+msg)
    for item in tosend_msg:
        con.send(item)
        tosend_msg.remove(item)
    with open(roll_number+".txt", "w") as f:
        for item in tosend_msg:
            f.writte("Sender: " + item.split(":")[0] + "\t Message : " + item.split(":")[1] + "\n")


#*****************************************FILE WRITING LEFT FOR BELOW METHODS************************************************

def decode_3001(con, data):
    #Single user message forward without multimedia
    #data="28 3001 04414802714 02714802714,Hey buddy how are you \n I am good here \n hope the same for you,29"

    actual=data[2:-2]
    code=actual[0:4]
    sender=actual.split(',')[0][4:15]
    reciever=actual.split(',')[0][15:]
    message=actual.split(',')[-2]
    print("Message: "+	 message)

    #with open("SingleUserMessages_3001.txt","a")as f:
    #	f.write("Sender: "+sender+"\tReciever: "+reciever+"\tMessage: "+message+"\n")
    with open(reciever+".txt","a")as f:
    	f.write("Sender: " + sender + "\tMessage: " + message + "\n")



def decode_3003(con, data):


    #Message intended for multiple users based on Regex ( 044 027 14)(this shows to reserve 3 3 and 2 characters resp for regex decoding)
    #    ***02714  : Cse of 2014 batch
    #    0C102714  : C1 batch of cse 2014
    #    ***027**  : All cse students of every year
    #data="28 3003 04414802714 ***02714,Hey student you all are stupid,29"

    actual = data[-2:2]
    code=actual[0:4]
    sender=actual.split(',')[0][4:15]
    reciever=actual.split(',')[0][15:]
    message=actual.split[1]
    tosend = rx.get_user(receiver)
    for item in tosend:
    	with open(item+".txt","a") as f:
    		f.write("Sender: " + sender+ "\t Message: " + message+"\n")


def decode_3002(con, data):


    #Single user message forward with multimedia
    #data="2830020441480271402902714802714:Hey student you all are stupid:IMAGE/VIDEO/PDF/TXT/AUDIO:29"
    #data="283002+-+-04414802714+-+-02902714802714+-+-Hey student you all are stupid+-+-IMAGE/VIDEO/PDF/TXT/AUDIO+-+-29"


    #actual = data[-2:2]
    #code=actual[0:4]
    #sender=actual.split('+-+-')[0][4:15]
    #reciever=actual.split('+-+-')[0][15:]
    #message=actual.split("+-+-")[-3]
    #media=actual.split("+-+-")[-2] #THIS IS TO BE SORTED OUT YET


    actual = data[2:-2]
    print("decode_3002 function called")
    code=actual[0:4]
    print("Actual is : "+actual)
    sender=actual.split("+-+-")[1]
    print("Sendr is: "+sender)
    reciever=actual.split("+-+-")[2]
    message=actual.split("+-+-")[3]
    media=actual.split("+-+-")[4]

    with open("MEDIA FILE.jpg","w")as fw:
    	fw.write(media)

#    print("Sender: "+sender+"\nReciever: "+reciever+"\nMessage: "+message+"\n")
    print("Sender : "+sender+"\treciever : "+reciever+"\tMessage: "+message+"\tMedia : "+media+"\n")



    #with open("MediaSingleReciever_3002.txt","a")as f:
    #	f.write("")
   

def decode_3004(con, data):


    #Message intended for multiple users based on Regex ( 044 027 14)(this shows to reserve 3 3 and 2 characters resp for regex decoding)
     #   ***02714  : Cse of 2014 batch
     #   0C102714  : C1 batch of cse 2014
     #   ***027**  : All cse students of every year
    #data="28 3005 04414802714 ***027**,Hey student you all are stupid,IMAGE/VIDEO/PDF/TXT/AUDIO,29"

    actual = data[-2:2]
    code=actual[0:4]
    sender=actual.split(',')[0][4:15]
    reciever=actual.split(',')[0][15:]
    message=actual.split[1]
    media=actual.split[2] #THIS IS TO BE SORTED OUT YET

def decode_3005(con, data):

    
    # THIS IS SPECIAL CASE OF ASSIGNMENTS(assignments/tutorials by teachers) 
    #Message intended for multiple users based on Regex ( 044 027 14)(this shows to reserve 3 3 and 2 characters resp for regex decoding)
      #  ***02714  : Cse of 2014 batch
     #  0C102714  : C1 batch of cse 2014
      #  ***027**  : All cse students of every year
    #data="28 3005 04414802714 ***027**,Description of Assignment ,Last date of submission ,IMAGE/VIDEO/PDF/TXT/AUDIO of assignment 29"

    actual = data[-2:2]
    code=actual[0:4]
    sender=actual.split(',')[0][4:15]
    reciever=actual.split(',')[0][15:]
    message=actual.split[1]
    last_Date=actual.split[2]
    media=actual.split[3] #THIS IS TO BE SORTED OUT YET
