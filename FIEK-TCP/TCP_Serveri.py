from _thread import *
import random
import datetime
import os
import socket
import sys
import math


host = 'localhost'
port = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind((host, port))
except socket.error:
    print("Klienti nuk mund të arrihet!")
    sys.exit()

serverSocket.listen(5)

print("Serveri eshte i gatshem te pranoj kerkesa")


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
        return "Eshte Palindrom!"
    else:
        return "Nuk eshte Palindrom!"

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


def fibonacci(number):
    x = 1
    y = 1
    for numeruesi in range(2, number):
        fibonacci = x + y;
        x = y;
        y = fibonacci;
    return fibonacci


def konvertimi(zgjedh, vlera):
    if zgjedh == "KilowattToHorsepower":
        rezultati = vlera * 1.3410220888

    elif zgjedh == "HorsepowerToKilowatt":
        rezultati = vlera * 0.73549875

    elif zgjedh == "DegreesToRadians":
        rezultati = vlera * (math.pi/180)

    elif zgjedh == "RadiansToDegrees":
        rezultati = vlera * (180/math.pi)

    elif zgjedh == "GallonsToLiters":
        rezultati = vlera * 3.785412

    elif zgjedh == "LitersToGallons":
        rezultati = vlera * 0.264172

    else:
        rezultati = "Gabim"
    return '%.2f'%(rezultati)


def clientthread(conn):
    while True:
        try:
            data = conn.recv(128).decode()
        except socket.error:
            print("Ka ndodhur një problem!")
            break

        merr = str(data).rsplit(" ")
        fjalia = ""
        i = len(merr)
        for fjala in range(1, i):
            fjalia = fjalia + merr[fjala]
            if (fjala != i):
                fjalia += " "
        if not data:
            break
        elif (merr[0] == "IPADRESA"):
            data = "IP Adresa e klientit është: " + address[0]
        elif (merr[0] == "NUMRIIPORTIT"):
            data = "Klienti eshte duke perdorur portin: " + str(address[1])
        elif (merr[0] == "BASHKETINGELLORE"):
            data = "Teksti i pranuar përmban " + str(bashketingellore(fjalia)) + " bashketingellore"
        elif (merr[0] == "PALINDROME"):
            data = "Teksti i shenuar: " + str(palindrome(fjalia.replace(" ", "")))
        elif (merr[0] == "DUPLIKIMI"):
            data = "Teksti pa shkronja duplikate eshte: " + str(removeDuplicate(fjalia))
        elif (merr[0] == "PRINTIMI"):
            data = "Print: " + str(printo(fjalia))
        elif (merr[0] == "HOST"):
            try:
                data = "Emri i hostit: " + str(socket.gethostbyaddr(host)[0])
            except socket.error:
                data = "Emri i hostit nuk u gjet!"
        elif (merr[0] == "KOHA"):
            data = "Data dhe koha aktuale eshte: " + str(datetime.datetime.now())
        elif (merr[0] == "LOJA"):
            data = "Numrat e gjeneruar jane: " + loja()
        elif (merr[0] == "FIBONACCI"):

            try:
                fjalia = int(merr[1])
            except Exception:
                break
            data = "Fibonacci: " + str(fibonacci(fjalia))
        elif (merr[0] == "KONVERTIMI"):
            try:
                numri = float(merr[2])
            except socket.error:
                break
            data = "Vlera e konvertuar eshte: " + str(konvertimi(merr[1], numri))

        else:
            data = "Serveri nuk mund t'i përgjigjet kësaj kërkese!"
        conn.send(data.encode())
    conn.close()


while 1:
    connection, address = serverSocket.accept()
    print("Në server është tani i lidhur:" + str(address))
    start_new_thread(clientthread, (connection,))

serverSocket.close()