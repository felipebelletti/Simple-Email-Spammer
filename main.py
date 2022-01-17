#!/usr/bin/python3
import smtplib
import sys

if len(sys.argv) != 5:
    print(sys.argv[0], "<email:password> <destination> <Message> <count>")
    sys.exit(1)

address = sys.argv[1]
destination = sys.argv[2]
message = sys.argv[3]
nn = int(sys.argv[4])

try:
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.ehlo()
    smtp.starttls()
    account = str(sys.argv[1]).split(":")
    print("\nLogging into "+str(account[0]))
    smtp.login(account[0], account[1])
    n = 0
    np = 1
    while n < nn:
        send = smtp.sendmail(address, destination, message)
        print("Sent", np, end='\r')
        np += 1
        n += 1
    print("")
    smtp.close()

except smtplib.SMTPAuthenticationError:
    sys.exit("\nAuthentication Error while Logging in "+str(account[0]))
except Exception as error:
    sys.exit(error)
