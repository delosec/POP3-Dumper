#!/usr/bin/python
import getpass 
import poplib
import sys

if len(sys.argv) < 4 or sys.argv[1].strip().lower() == "--help":
    print("Pop3 dumper:\n"+sys.argv[0]+"username password ip port")
    exit()

username = sys.argv[1]
password = sys.argv[2]
ip       = sys.argv[3]
port     = sys.argv[4]
 
Mailbox = poplib.POP3(ip, port) 
Mailbox.user(username) 
Mailbox.pass_(password) 
numMessages = len(Mailbox.list()[1])
for i in range(numMessages):
    for msg in Mailbox.retr(i+1)[1]:
        print msg
Mailbox.quit()
