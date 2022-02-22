# This .py file is to get the sensors from the sensors and store them in the SQL database
# This file would run alongside app.py so that we have dynamic data 

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

import mysql.connector as mysql
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO # raspberry pi
import time
import Freenove_DHT as DHT # temp sensor
from PCF8574 import PCF8574_GPIO #LCD
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

DHTPin = 11     #define the pin of DHT11
trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout according to the maximum measuring distance

 
load_dotenv('credentials.env')
 
''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

''' Distance Ultrasonic sensor'''
def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     # get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level 
    time.sleep(0.00001)     # 10us
    GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level 
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s 
    return distance
    
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    GPIO.setup(trigPin, GPIO.OUT)   # set trigPin to OUTPUT mode
    GPIO.setup(echoPin, GPIO.IN)    # set echoPin to INPUT mode

''' Store in SQL'''
def store_sensor_data(distance, temperature): # for SQL table
    #connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()
 
    # insert data
    insert_stmt = ("INSERT INTO SensorData (distance, temperature) VALUES (%s, %s);")
    data = (distance, temperature)
    cursor.execute(insert_stmt, data)
    db.commit()
    
''' Getting live data'''    
def loop():
    

    dht = DHT.DHT(DHTPin)   #create a DHT class object
    counts = 0 # Measurement counts
    while(True): # for endless loop: while(True) ; for limited counts < 20
      # temperature	
      counts += 1
      print("Measurement count: ", counts)
      for i in range(0,15):            
          chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
          if (chk is dht.DHTLIB_OK):  #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
              print("DHT11,OK!")
              break
          time.sleep(0.1)
      print("Temperature : %.2f"%(dht.temperature))
      
      # distance
      distance = getSonar() # get distance
      print ("The distance is : %.2f cm\n"%(distance))
        
      # insert dist and temp into SQL table
      store_sensor_data(distance, dht.temperature) 

      time.sleep(2)



if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  
