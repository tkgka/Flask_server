from flask import Flask, request, render_template, redirect, url_for
import flask
import os
import imgkit
import json
options = {
    'format': 'png',
    'height': 500, 
    'encoding': "UTF-8",
}

app = Flask(__name__)
 
@app.route("/")
def fullurl():
    url = request.args.get('url')
    if url != None:
        stream = os.popen('curl --head "'+url+'" | grep Location')
        output= flask.Response(stream.read())
        output.headers["Access-Control-Allow-Origin"] = "*"        
        return output
    
    else:
        return "None"
@app.route("/img/")
def img():    
    url = request.args.get('url')
    img = imgkit.from_url(url, False, options=options)
    return flask.Response(img, mimetype="image/png")

if __name__ == "__main__":
    app.debug = True
    app.run()