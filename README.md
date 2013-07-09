BFGMiner-SMSMonitor
===================

A simple python script that connects to BFGMiner and monitors the status of your mining hardware.  If any devices drop off, it can restart BFGMiner and send you either an SMS, E-Mail or both.

This is a work in progress, and was originally written by a friend.  PolrPaul from the Butterfly Labs forum also helped out a bunch by including SMS messagins via Google Voice.

*I have been using this with BFGMiner 3.1.1 on OSX using both ButteFly Labs SC Singles and their BitForce FPGA Singles, so I haven't tested it with any other hardware.*

*It should work with CGMiner, but I haven't tested it.*


REQUIREMENTS
------------

* Python (I'm using 2.7.2 on OSX Lion)
* [pygooglevoice](https://code.google.com/p/pygooglevoice/)
* [Google Voice Account](https://voice.google.com)
* Email account/server

*With OSX, [there is a fix](https://code.google.com/r/bwpayne-pygooglevoice-auth-fix/source/checkout) to get Google Voice working.*

SETUP
-----

Pretty self explanitory in the source comments.

Change the User Variables to whatever you want for:

* BFGMiner Host & Port
* Number of Device to Monitor
* SMS Number
* SMS Messsage
* Timeout (in seconds)
* E-Mail information

*Single SCs are seen as 16 devices, BitForce FPGA singles are seen as one device.*

*Right now it has the email functions commented out, so it'll only send SMS messages (I Hate waking up to a bajillion emails telling me something is wrong, when an SMS would have woken me up instead).  Uncomment the email lines on line 1220 & 121 to turn this on, but be warned, it will email you after every timeout once a problem is detected.*


RUNNING
-------

Initiate it by running:

    python STATUS.py

Kill it with a ctrl-c
