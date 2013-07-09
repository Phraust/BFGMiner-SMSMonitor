BFGMiner-SMSMonitor
===================

A simple python script that connects to BFGMiner and monitors the status of your mining hardware.  If any devices drop off, it can restart CGMiner and send you either an SMS, E-Mail or both.

This is a work in progress, and was originally written by a friend.  PolrPaul from the ButterFly Labs forum also helped out a bunch by including SMS messagins via Google Voice.


REQUIREMENTS
============

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
=====

Pretty self explanitory in the source comments.

Change the User Variables to whatever you want for your BFGMiner Host & Port, SMS Number, SMS Messsage, Timeout (in seconds) and email information.

Initiate it by running: python STATUS.py
