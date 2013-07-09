#!/usr/bin/python
 
# IMPORTS
import socket
import string
import time
import datetime
import os
from smtplib import SMTP
from decimal import *
 
from googlevoice import Voice
from googlevoice.util import input
 
 
# USER VARIABLES

SMS_NUMBER = '(123)456-7890'      # Mobile number to receive SMS
SMS_MESSAGE = 'HELP :('           # Message you want to receive
 
NUMBER_OF_LIVE_DEVICES = 1        # Number of devices to monitor
TIMEOUT = 60                      # Seconds between checks
TCP_IP = '127.0.0.1'              # IP of BFGMiner instance to monitor
TCP_PORT = 4028                   # Port # of BFGMiner to monitor
 
FROM_EMAIL = ''                   # E-Mail address to send from
TO_EMAIL = ''                     # E-Mail address to send to
EMAIL_SERVER = ''                 # E-Mail server to send from
PASSWORD = ''                     # E-Mail password
 
 
# BASE VARIABLES

BUFFER_SIZE = 102433
COUNT = 0
REBOOTS = 0
e = 0
errors = 0
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
 
 
# FUNCTIONS

def cls():
        os.system(['clear','cls'][os.name == 'nt'])
 
def getLiveDevices():
    try :
        MESSAGE="devs"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()
        #print data
        return string.count(data, "Alive")
    except:
        return 0
 
def rebootMiner():
    try:
        MESSAGE="restart"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()
        return string.count(data, "Alive")
    except:
        return 0
 
def sendemail():
    smtp = SMTP()
    smtp.connect(EMAIL_SERVER , 25)
    smtp.login(FROM_EMAIL , PASSWORD)
 
    subj = "MINER DOWN"
    date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    message_text = "SOMETHING IS WRONG."
    msg = "From: %s\nTo: %s/nSubject: %s\nDate: %s\n\n%s" % (FROM_EMAIL , TO_EMAIL , subj , date, message_text )
 
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, msg)
 
def sendsms():
    voice = Voice()
    voice.login()
 
    phoneNumber = SMS_NUMBER
    text = SMS_MESSAGE
 
    voice.send_sms(phoneNumber, text)
 
 
# START
cls()
print "STARTING AT" + bcolors.OKBLUE , datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") , bcolors.ENDC
print "CHECKING FOR" + bcolors.OKBLUE , NUMBER_OF_LIVE_DEVICES , bcolors.ENDC + "DEVICES."
print "CHECKING HOST" + bcolors.OKBLUE , TCP_IP , bcolors.ENDC
print "RECHECKING EVERY" + bcolors.OKBLUE , TIMEOUT , bcolors.ENDC +  "SECONDS."
print "\n"
 
 
# LOOP
 
while(1):
        time.sleep(TIMEOUT)
        try:
                if (getLiveDevices() < NUMBER_OF_LIVE_DEVICES):
                        if errors > 2:
                                cls()
# Uncomment to send E-Mail

#                               sendemail()
#                               print bcolors.WARNING + "EMAIL SENT. RESTARTING MINER." + bcolors.ENDC

                                sendsms()
                                print bcolors.WARNING + "SMS SENT. RESTARTING MINER." + bcolors.ENDC
                                REBOOTS +=1
                                COUNT = 0
                                errors = 0
                                rebootMiner()
                        elif errors <= 2:
                                cls()
                                COUNT = 0
                                errors +=1
                                print bcolors.FAIL + str(errors) , "FAILURES."
                                print "RETRY IN " + str(TIMEOUT) , "SECONDS." + bcolors.ENDC
                else:
                        cls()
                        COUNT += 1
                        print bcolors.OKBLUE + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + bcolors.ENDC
                        print "STATUS:" + bcolors.OKGREEN , "OK" , bcolors.ENDC
                        print bcolors.OKBLUE + str(getLiveDevices()) + bcolors.ENDC + " OF " + bcolors.OKBLUE + str(NUMBER_OF_LIVE_DEVICES) + bcolors.ENDC , "DEVICES UP FOR" , bcolors.OKBLUE + str(round((COUNT*TIMEOUT)/60.00/60.00, 2)) , bcolors.ENDC + "HOURS."
                        #print bcolors.FAIL + str(REBOOTS) + bcolors.ENDC , 'REBOOTS.'
                        print "CHECK" , bcolors.FAIL + "#"+  str(COUNT) + bcolors.ENDC , "IN " + bcolors.OKBLUE + str(TIMEOUT) + bcolors.ENDC , "SECONDS."
                        print "\n"
                        errors = 0
        except e:
                print bcolors.FAIL + e , "MINER IS DEAD."
