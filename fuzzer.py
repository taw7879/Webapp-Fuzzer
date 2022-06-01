# AE Fuzzer Project for BodgeIt Store

import socket
import os
import time
import random

os.system("cls")
host = "127.0.0.1"
port = 8080

#try:
print("Attempting connection to BodgeIt Store...")
time.sleep(1)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(3)
client_socket.connect((host, port))
os.system("cls")

print("Successfully connected to BodgeIt Store!\n")

while True:
    option = int(input("Send random string or SQLi/XSS commands? (1 or 2) "))

    if option == 1:
        length = int(input("\nEnter string length: "))
        bad = ""
        for i in range(length):
            j = random.randint(32, 126)
            bad += chr(j)

        print("\nSending random string of length " + str(length) + " to BodgeIt Store...")
        client_socket.send(bad.encode())
        print("\nMessage successfully sent..\n")
        time.sleep(1)

        try:
            msg = client_socket.recv(1024)
            print("Server:\n" + msg.decode())
            print("\nString sent: " + bad)
        except:
            print("Server sent no response")

    elif option == 2:
        commands = ["something%0Acat%20/etc/passwd", "ping%PROGRAMFILES:~10,-5%IP", "ping%CommonProgramFiles:~10,-18%IP", "%%2727", "%25%27", "`+HERP", "'+'herp", "' 'DERP", "'%20'HERP", "'%2B'HERP"]
        index = random.randint(0, len(commands)-1)
        command = commands[index]
        print("\nSending \"" + command + "\"" + " to BodgeIt Store...")
        client_socket.send(command.encode())
        print("\nCommand successfully sent..\n")
        time.sleep(1)
        
        try:
            msg = client_socket.recv(1024)
            print("Server:\n" + msg.decode())
        except:
            print("Server sent no response")
    
    else:
        continue

    again = int(input("\nSend another response? (1 for yes, 2 for no) "))
    if again != 1:
        break
    else:
        os.system("cls")

#except:
    #os.system("cls")
    #print("Failed to connect or Connection stopped to BodgeIt Store...")
    #time.sleep(2)
    #os.system("cls")


client_socket.close()