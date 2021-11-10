from flask import Flask, request
import flask
import os
app = Flask(__name__)
 
@app.route("/")
def hello():
    url = request.args.get('url')
    if url != None:
        stream = os.popen('curl --head "'+url+'" | grep Location')
        output= flask.Response(stream.read())
        output.headers["Access-Control-Allow-Origin"] = "*"
        return output
    else:
        return "None"