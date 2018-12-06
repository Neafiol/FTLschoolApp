import sys
import urllib

from datashape import json

sys.path.append('../')


from models import Puple,Messages
from  bottle import Bottle, request, response, run, static_file, template
app = Bottle()

@app.post("/enter")
def close_qst():
    rec = urllib.parse.parse_qs(request.body.read().decode())

    log=rec.get('login')[0]
    pas=rec.get('password')[0]
    print(log)
    if len(Puple.select().where(Puple.login==log,Puple.password==pas))>0:
        return 'true'
    return 'false'

@app.post("/reg")
def close_qst():
    rec = urllib.parse.parse_qs(request.body.read().decode())

    try:
        log = rec.get('login')[0]
        pas = rec.get('password')[0]
        print(log,pas)
        if len(Puple.select().where(Puple.login==log and Puple.password==pas))>0:
            return 'false'


        puple = Puple( login = rec.get('login')[0],password=rec.get('password')[0],name=rec.get('name')[0],
                       surname=rec.get('surname')[0], email=rec.get('email')[0],phone=rec.get('phone')[0],
                       class_nom=rec.get('class_nom')[0],class_type=rec.get('class_type')[0])
        puple.save()

        return 'true'
    except:
        return 'false'


@app.post("/get_message")
def close_qst():
    rec = urllib.parse.parse_qs(request.body.read().decode())

    log = rec.get('login')
    puple=Puple.select().where(Puple.login==log)[0]
    clas=puple[6]
    letter=puple[7]

    mes=Messages.select().where(Messages.puple_id==log)
    mes.append()

    return 'true'


@app.get("/enter")
def close_qst():
    print('get:'+str(request.GET.get('username')))
    data = 'ok'
    return str(data)


@app.get("<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")
@app.get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'



@app.route('/<name:re:[0-9]*>')
def show_news(name):
    return template('data.html')

    pass
#host='0.0.0.0'
run(app,port=8077)
