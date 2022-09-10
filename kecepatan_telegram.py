from email import message
import requests
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setwarnings (False)
GPIO.setup(37,GPIO.OUT)
 
TOKEN = '5752462236:AAHlALX-witMAtc4U8GAj2Pft06P2I1zanA'
chat_id = '-654097079'

message = "Anda MELEBIHI batas kecepatan yang telah ditentukan!"
message2 = "Anda mengendarai dalam kecepatan yang aman!"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

while True:
    if GPIO.input(8)==0:
       GPIO.output(37,True)
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
       print(requests.get(url).json()) #this send the message
    else :
        GPIO.output(37,False)
        time.sleep(0.1)
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
#         print(requests.get(url).json()) #this send the message