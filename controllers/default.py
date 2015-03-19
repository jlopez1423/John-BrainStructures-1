import gluon.contrib.simplejson
import json
import wikipedia

def getwikisummary():
    name = request.vars['name']
    try:
        content = wikipedia.summary(name)
    except:
        content = "No data for this region."
        pass
    return json.dumps(content)

def index():

    return dict()
