import socket
import sys
from _thread import *
import random
import datetime
import math

print("----------------------------UDP SERVERI-----------------------")
host = 'localhost'
port = 11000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    serverSocket.bind((host, port))

except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()

print("Serveri tani eshte i gatshem per pranimin e kerkesave")
print("--------------------------------------------------------------")


def bashketingellore(text):
  zanoret = ['A', 'E', 'I', 'O', 'U', 'Y']
  bashketingelloret = 0
  for character in text:
    if character.isalpha():
      if character.upper() not in zanoret:
        bashketingelloret += 1
  return bashketingelloret;


def palindrome(s):
    r = s[::-1]
    if s == r:
        return True
    else:
        return False

def removeDuplicate(text):
    newStr = ""
    for ch in text:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr


def printo(print):
    print = (str(print)).strip()
    return print


def loja():
    numrat = ""
    for number in range(0, 7):
        randomNumber = random.randint(1, 49)
        numrat += str(randomNumber) + ", "
    return numrat


def fibonacci(numri):
    x = 1
    y = 1
    for numeruesi in range(2, numri):
        fibonacci = x + y;
        x = y;
        y = fibonacci;
    fibonacciString = str(fibonacci)
    return fibonacciString


def konverto(zgjedh, vlera):
    if zgjedh == "KilowattToHorsepower":
        Horsepower = vlera * 1.3410220888
        HorsepowerString = str(Horsepower)
        return HorsepowerString


    elif zgjedh == "HorsepowerToKilowatt":
        Kilowatt = vlera * 0.73549875
        KilowattString = str(Kilowatt)
        return KilowattString



    elif zgjedh == "DegreesToRadians":
        Radians = vlera * (math.pi / 180)
        RadiansString = str(Radians)
        return RadiansString


    elif zgjedh == "RadiansToDegrees":
        Degrees = vlera * (180 / math.pi)
        Degreestring = str(Degrees)
        return Degreestring



    elif zgjedh == "GallonsToLiters":
        Liters = vlera * 3.785412
        LitersString = str(Liters)
        return LitersString


    elif zgjedh == "LitersToGallons":
        Gallons = vlera * 0.264172
        GallonsString = str(Gallons)
        return GallonsString


def clientthread(input, address):
    try:
        data = input.decode()
    except socket.error:
        print("A problem has occurred!")

    merr = str(data).rsplit(" ")
    fjalia = ""
    i = len(merr)
    for fjala in range(1, i):
        fjalia = fjalia + merr[fjala]
        if (fjala != i):
            fjalia += " "
    if not data:
        return
    elif (merr[0] == "IPADRESA"):
        data = "IP Adresa e klientit eshte: " + address[0]
    elif (merr[0] == "NUMRIIPORTIT"):
        data = "Klienti eshte duke perdorur portin: " + str(address[1])
    elif (merr[0] == "BASHKETINGELLORE"):
        data = "Teksti i pranuar përmban " + str(bashketingellore(fjalia)) + " bashketingellore"
    elif (merr[0] == "PALINDROME"):
        data = "Eshte palindrom: " + str(palindrome(fjalia.replace(" ", "")))
    elif (merr[0] == "DUPLIKIMI"):
        data = "Fjalia: " + str(removeDuplicate(fjalia))
    elif (merr[0] == "PRINTIMI"):
        data = "Print: " + str(printo(fjalia))
    elif (merr[0] == "HOST"):
        try:
            data = "Emri i hostit: " + str(socket.gethostbyaddr(host)[0])
        except socket.error:
            data = "Host's name not found!"
    elif (merr[0] == "KOHA"):
        data = "Data dhe koha aktuale eshte: " + str(datetime.datetime.now())
    elif (merr[0] == "LOJA"):
        data = "Jane gjeneruar keta numra: " + loja()
    elif (merr[0] == "FIBONACCI"):
        try:
            vlera = int(merr[1])
        except Exception:
            return
        data = "Fibonacci: " + str(fibonacci(vlera))
    elif (merr[0] == "KONVERTIMI"):
        try:
            numri = float(merr[2])
        except socket.error:
            return
        data = "Vlera e konvertuar: " + str(konverto(merr[1], numri))

    else:
        data = "The server can't respond to this request! Serveri nuk mund ti pergjigjet kesaj kerkese"
    serverSocket.sendto(data.encode(), address)


while 1:
    data, address = serverSocket.recvfrom(128)
    print("Kerkese e re per: " + str(address))
    start_new_thread(clientthread, (data, address,))

serverSocket.close()