BFGMiner-SMSMonitor
===================

A simple python script that connects to BFGMiner and monitors the status of your mining hardware.  If any devices drop off, it can restart CGMiner and send you either an SMS, E-Mail or both.

This is a work in progress, and was originally written by a friend.  PolrPaul from the ButterFly Labs forum also helped out a bunch by including SMS messagins via Google Voice.

*I have been using this with BFGMiner 3.1.1 on OSX using both ButteFly Labs SC Singles and their BitForce FPGA Singles, so I haven't tested it with any other hardware.

*It should work with CGMiner, but I haven't tested it.


REQUIREMENTS
------------

Python
I'm using 2.7.2 on OSX Lion

pygooglevoice
https://code.google.com/p/pygooglevoice/

for OSX, there is a fix to get it working
https://code.google.com/r/bwpayne-pygooglevoice-auth-fix/source/checkout

Email account/server
For sending emails.

Goovle Voice Account
For sending SMS Messages.


SETUP
-----

Pretty self explanitory in the source comments.

Change the User Variables to whatever you want for your BFGMiner Host & Port, SMS Number, SMS Messsage, Timeout (in seconds) and email information.

*Right now it has the email functions commented out, so it'll only send SMS messages (I Hate waking up to a bajillion emails telling me something is wrong, when an SMS would have woken me up instead).  Uncomment the email lines on line 122 &122 to turn this on, but be warned, it will email you after every timeout once a problem is detected.

RUNNING
-------

Initiate it by running:
    python STATUS.py

Kill it with a ctrl-c
