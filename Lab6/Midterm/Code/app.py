# server-side backend (python & REST) - THE WEB DEVELOPMENT PART

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
from pyramid.renderers import render_to_response
import collections

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
import json
 
load_dotenv('credentials.env')
 
''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

# input condition 1: get highest, lowest, average temp
def get_temp(req):

    data = json.loads(req.body.decode("utf-8"))
    input = str(data["temperature"]) # gets input : highest, lowest or average
   
    a = '"highest"'
    b = '"lowest"'
    c = '"average"'
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()
    if (input == a):
        cursor.execute("SELECT MAX(temperature) FROM SensorData ;" )
        record = cursor.fetchone()
        db.close()
        if record is None:
            return {
                'error': "No data was found for the given ID",
                'temperature': ""
            }
         # populate json with values
        response = {
            'temperature': record[0]
        }   

        return response


    elif input == b:
        cursor.execute("SELECT MIN(temperature) FROM SensorData ;" )
        record = cursor.fetchone()
        db.close()
       
        if record is None:
            return {
                'error': "No data was found for the given ID",
                'temperature': ""
            }   
         # populate json with values
        response = {
            'temperature': record[0]
        }   

        return response
    elif input == c:
        cursor.execute("SELECT AVG(temperature) FROM SensorData ;" )
        record = cursor.fetchone()
        db.close()
        if record is None:
            return {
                'error': "No data was found for the given ID",
                'temperature': ""
            }
         # populate json with values
        response = {
            'temperature': record[0]
        }   

        return response



# input condition 3: get the current data for all data columns when you click on the button
def get_data(req):

    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute("SELECT * FROM SensorData ORDER BY id DESC LIMIT 1;" )
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'id': "",
            'created_at': "",
            'distance': "",
            'temperature': ""
        }

    # populate json with values
    response = {
        'id': record[0],
        'created_at': str(record[1]),
        'distance': record[2],
        'temperature': record[3]
    }

    return response

def get_data1():

    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute("SELECT temperature FROM SensorData ORDER BY id DESC LIMIT 1;" )
    record = cursor.fetchone()
    db.close()

    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'temperature': ""
        }

    # populate json with values
    response = {
        'temperature': record[0]
    }

    return response

# test: how to display sql table using Jinja

def get_home(req):
  return FileResponse("index.html")




def get_datarows(req):
  data = json.loads(req.body.decode("utf-8"))
  input = str(data["rows"]) # gets input : 2, 4, 6
  print("input from Java "+input)
  a = '2'
  b = '4'
  c = '6'
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  if (input == a):
        cursor.execute("SELECT * FROM SensorData ORDER BY id DESC LIMIT 2;" )
        record = cursor.fetchall()
        db.close()
        if record is None:
            return {
                'error': "No data was found for the given ID",
            }

        objects_list = []
        for row in record:
            d = collections.OrderedDict()
            d["id"] = str(row[0])
            d["time"] = str(row[1])
            d["distance"] =str(row[2])
            d["temperature"] = str(row[3])
            objects_list.append(d)
        response = json.dumps(objects_list)
        return response
  elif input == b:
        cursor.execute("SELECT * FROM SensorData ORDER BY id DESC LIMIT 4;" )
        record = cursor.fetchall()
        db.close()
        if record is None:
            return {
                'error': "No data was found for the given ID",
            }
        objects_list = []
        for row in record:
            d = collections.OrderedDict()
            d["id"] = str(row[0])
            d["time"] = str(row[1])
            d["distance"] = str(row[2])
            d["temperature"] = str(row[3])
            objects_list.append(d)
        response = json.dumps(objects_list)
        
        return response
  elif input == c:
        cursor.execute("SELECT * FROM SensorData ORDER BY id DESC LIMIT 6;" )
        record = cursor.fetchall()
        db.close()
        if record is None:
            return {
                'error': "No data was found for the given ID",
            }
        objects_list = []
        for row in record:
            d = collections.OrderedDict()
            d["id"] = str(row[0])
            d["time"] = str(row[1])
            d["distance"] = str(row[2])
            d["temperature"] = str(row[3])
            objects_list.append(d)
        response = json.dumps(objects_list)
        return response

def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

    
def display_LCD(req):
    # set board connection
    PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
    

    try: # Create PCF8574 GPIO adapter.
        mcp = PCF8574_GPIO(PCF8574_address)
    except:
        try:
            mcp = PCF8574_GPIO(PCF8574A_address)
        except:
            print ('I2C Address Error !')
            exit(1)

    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns

    

    # get the data
    lcd.setCursor(0,0)  # set cursor position
    record = get_data1()
    print(record)
    lcd.message( 'Temp: ' + str(record["temperature"])+'\n' )# display temperature
    lcd.message( get_time_now() )   # display the time
    sleep(2)
    return {
            'Display': "ON"
        }



if __name__ == '__main__':
    with Configurator() as config:
        # to use jinja
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')

        # add routes
        config.add_route('home', '/') #adds route to home page
        config.add_view(get_home, route_name='home')

        config.add_route('data', '/data') #show current data when you click on the button
        config.add_view(get_data, route_name='data', renderer='json')
        
        config.add_route('temperature', '/temperature')
        config.add_view(get_temp, route_name='temperature', renderer='json')

        config.add_route('datarows', '/datarows')
        config.add_view(get_datarows, route_name='datarows', renderer='json')

        config.add_route('display', '/display')
        config.add_view(display_LCD, route_name='display', renderer='json')
        
        

        # static assets
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

server = make_server('0.0.0.0', 6543, app)
print('Web server started on: http://0.0.0.0:6543')
server.serve_forever()