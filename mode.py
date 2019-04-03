import RPi.GPIO as gp
import time 
import requests as req

gp.setmode(gp.BOARD)

url = 'https://vendingpi.herokuapp.com'

cokePrice = '20'
LaysPrice = '10'
KitKatPrice = '10'
DairyMilk = '30'

motor1 = 3 #Coke
motor2 = 5 #Lays
motor3 = 7 #Kitkat
motor4 = 11 #Dairy

cardSuccess = 19
Mode = 21

gp.setup(motor1, gp.OUT)
gp.setup(motor2, gp.OUT)
gp.setup(motor3, gp.OUT)
gp.setup(motor4, gp.OUT)
gp.setup(cardSuccess, gp.IN)
gp.setup(Mode, gp.OUT)

user1 = "X9JiHpsDt9OioCmBiX1VwSwiq7m2"  # Rohan
user2 = "Yet2jm7a5nOlc9c1cXYChcHl6cp1"  # Dhanush
user3 = "cpqSQeFfnMf6HrKwGIv2f0TcQB72"  # Shireesh
user4 = "ktIzXYFnnwZrqL1UQy23j226dLz2"  # Raghav

priceArray = [cokePrice, LaysPrice, KitKatPrice, DairyMilk]

delayValue = 1

def getMode():
    r = req.get(url + '/api' + '/get' + '/mode')
    k = r.json()
    return k


def updateItemCount(name):
    r = req.post(url + '/api' + '/update' + '/item/' + name)
    d = r.text
    print(d)


def updateWalletBalance(userId, price):
    r = req.post(url + '/api' + '/update/' + 'wallet/' + userId + '/' + price)
    d = r.text
    return d

def setMode(mode):
   r = req.post(url + '/api' + '/set' + '/mode/' + mode)
   d = r.text
   print (d)

if __name__ == '__main__':
    k = True
    setMode('Temp')
    while k:
        f = getMode()
        mode = f['mode']
        user = f['user']
        selected = f['selected']
        phoneBuy = f['phoneBuy']
        if mode == 'Card' and phoneBuy == False:
            gp.output(Mode, 1)
            if gp.input(cardSuccess) == 1:
                f = updateWalletBalance(user, priceArray[int(selected) - 1])
                print(f)
                if selected == 1:
                  print('Motor 1 ON')
                  gp.output(motor1,1)
                elif selected == 2:
                  print('Motor 2 ON')
                  gp.output(motor2,1)
                elif selected == 3:
                  print('Motor 3 ON')
                  gp.output(motor3,1)
                elif selected == 4:
                  print('Motor 4 ON')
                  gp.output(motor4,1)
                if f == 'OK':
                  setMode('Temp')
        elif mode == 'Temp' and phoneBuy == True:
              if selected == 1:
        else:
            print('Waiting')
