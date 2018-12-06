import sys
import urllib

sys.path.append('../')


from models import Puple
from  bottle import *

@post("/enter")
def close_qst():

    rec = urllib.parse.parse_qs(request.body.read().decode())
    name=rec.get('username')[0]
    print(name)

    return "'ewewew'"

@get("/enter")
def close_qst():
    print('get:'+str(request.GET.get('username')))
    return "{name:'petya'}"


@get("<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")
@get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")



@route('/<name:re:[0-9]*>')
def show_news(name):
    return template('data.html')

    pass
#host='0.0.0.0'
run(port=8077)
