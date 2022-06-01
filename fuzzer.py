# AE Fuzzer Project for BodgeIt Store

import socket
import os
import time

os.system("cls")
host = "127.0.0.1"
port = 8080

try:
    print("Attempting connection to BodgeIt Store...")
    time.sleep(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(3)
    # set timeout on subsequent blocking methods (connect, recv)
    # recv's operation is not complete within 3 seconds, an exception will be raised
    client_socket.connect((host, port))
    os.system("cls")

    print("Successfully connected to BodgeIt Store!\n")
    length = input("Enter string length: ")
    res = ''
    print("\nSending random string of length " + length + " to BodgeitStore...")

    msg = client_socket.recv(1024)
    print("Server: " + msg.decode())



except:
    os.system("cls")
    print("Failed to connect to BodgeIt Store...")
    time.sleep(2)
    os.system("cls")




#length = input("String length: ")
#print("\nSending random string of length " + length + " to BodgeitStore...")
#time.sleep(3)


