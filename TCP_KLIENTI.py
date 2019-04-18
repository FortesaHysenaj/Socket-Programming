import socket
import sys
import io

host='localhost'
port=12000

socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketClient.connect((host,port))
print("------------------------TCP KLIENTI-------------------------------------")
print("Zgjedhni nje metode: \nIPADRESA\nNUMRIIPORTIT\nHOST\nBASHKETINGELLORE (+shkruaj nje fjale-fjali)\n"
      "\nPRINTIMI (+shkruaj nje fjale/fjali)\nPALINDROME (+shkruaj nje fjale-fjali)\nDUPLIKIMI (+shkruaj nje fjale-fjali)\n"
      "KOHA\nLOJA\nFIBONACCI (nr>2)\nKONVERTIMI [(KilowattToHorsepower, HorsepowerToKilowatt,\n "
      "DegreesToRadians, RadiansToDegrees,\n GallonsToLiters, LitersToGallons)+vlera]")
print("-------------------------------------------------------------------------")
message=input("OPERACIONI >>> ")
while(message!='Q' and (message !="")):
        socketClient.send(message.encode())
        data=socketClient.recv(128).decode()
        '''
        if not data:
            print("Kjo mundesi nuk ekziston")
            message=input("OPERACIONI >>> ")
            continue
        '''
        print(data)
        message=input("OPERACIONI >>> ")

socketClient.close();