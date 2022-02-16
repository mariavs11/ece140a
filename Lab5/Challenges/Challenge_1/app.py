from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse
import mysql.connector as mysql
from dotenv import load_dotenv
import os
import json

load_dotenv('credentials.env')

''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


# this function will query data under the conditions of height and age
def get_info(req):
    # get the id from the request
    data = json.loads(req.body.decode("utf-8")) # gets data from rest.js
    range_h = data["height"].split('-')
    lower_h = int(range_h[0])
    upper_h = int(range_h[1])
    range_a = data["age"].split('-')
    lower_a = int(range_a[0])
    upper_a = int(range_a[1])
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute("SELECT ID,Name, Owner, Height, Age FROM Gallery_Details WHERE (Height>=%d AND Height< %d) AND (Age>=%d AND Age<%d);" % (lower_h,upper_h, lower_a, upper_a))
    record = cursor.fetchone()
    db.close()


    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'ID': "",
            'Name': "",
            'Owner': "",
            'Age': ""
        }

    # populate json with values
    response = {
        'ID': record[0],
        'Name': record[1],
        'Owner': record[2],
        'Height': record[3],
        'Age': record[4]
    }

    return response


# this function will query data under the conditions of height
def get_height(req):
    # get the id from the request
    data = json.loads(req.body.decode("utf-8"))
    range_h = data["height"].split('-')
    lower_h = int(range_h[0]) # gets lower limit of height
    upper_h = int(range_h[1]) # gets upper limit of height
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database
    cursor.execute("SELECT ID,Name, Owner, Height, Age FROM Gallery_Details WHERE (Height>=%d AND Height< %d) ;" % (lower_h,upper_h))
    record = cursor.fetchone()
    db.close()


    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'ID': "",
            'Name': "",
            'Owner': "",
            'Age': ""
        }

    # populate json with values
    response = {
        'ID': record[0],
        'Name': record[1],
        'Owner': record[2],
        'Height': record[3],
        'Age': record[4]
    }

    return response


# this function will query data under the conditions of age
def get_age(req):

    data = json.loads(req.body.decode("utf-8"))
    range_a = data["age"].split('-')
    lower_a = int(range_a[0]) # gets lower limit of age
    upper_a = int(range_a[1]) # gets upper limit of age
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute("SELECT ID,Name, Owner, Height, Age FROM Gallery_Details WHERE (Age>=%d AND Age<%d);" % ( lower_a, upper_a))
    record = cursor.fetchone()
    db.close()


    # if no record found, return error json
    if record is None:
        return {
            'error': "No data was found for the given ID",
            'ID': "",
            'Name': "",
            'Owner': "",
            'Age': ""
        }

    # populate json with values
    response = {
        'ID': record[0],
        'Name': record[1],
        'Owner': record[2],
        'Height': record[3],
        'Age': record[4]
    }

    return response




def get_home(req):
  return FileResponse("index.html")


if __name__ == '__main__':
    with Configurator() as config:
        # Create a route called home
        config.add_route('home', '/')
        # Bind the view (defined by index_page) to the route named ‘home’
        config.add_view(get_home, route_name='home')

        # Create a route that handles server HTTP requests at:
        config.add_route('photos', '/photos') # route created to query data based on height and age parameters
        config.add_view(get_info, route_name='photos', renderer='json') # triggers get_info
        config.add_route('height', '/height') # route created to query data based on height parameters
        config.add_view(get_height, route_name='height', renderer='json')  # triggers get_height
        config.add_route('age', '/age') # route created to query data based on age parameters
        config.add_view(get_age, route_name='age', renderer='json') # triggers get_age
        # Add a static view
        # This command maps the folder “./public” to the URL “/"
        config.add_static_view(name='/', path='./public', cache_max_age=3600)

        # Create an app with the configuration specified above
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)  # Start the application on port 6543
    server.serve_forever()



