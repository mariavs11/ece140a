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

geisel_photos = [
 {"id":1, "img_src": "geisel-1.jpg"},
 {"id":2, "img_src": "geisel-2.jpg"},
 {"id":3, "img_src": "geisel-3.jpg"},
 {"id":4, "img_src": "geisel-4.jpg"},
 {"id":5, "img_src": "geisel-5.jpg"},
] # has 5 JSON VALUES, 2 key-value pairs: id and img_scr


def get_info(req):
    # get the id from the request
    data = json.loads(req.body.decode("utf-8"))
    range_h = data["height"].split('-')
    lower_h = range_h[0]
    upper_h = range_h[1]
    range_a = data["age"].split('-')
    lower_a = range_a[0]
    upper_a = range_a[1]
    # connect to the database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # query the database with the id
    cursor.execute("SELECT ID,Name, Owner, Height, Age FROM Gallery_Details WHERE (Height>=%d AND Height< %d) OR (Age>=%d AND Age<%d)';" % (lower_h,upper_h, lower_a, upper_a))
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

def get_photo(req):
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/') # adds route to home page
        config.add_view(get_home, route_name='home')
        config.add_route('get_info', '/photos')
        config.add_view(get_info, route_name='get_info', renderer='json')

        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()

server = make_server('0.0.0.0', 6542, app)
print('Web server started on: http://0.0.0.0:6542')
server.serve_forever()

