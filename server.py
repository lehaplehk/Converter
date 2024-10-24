# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify, send_file
from flask import render_template, request, redirect, url_for, flash, make_response, session
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime, timedelta, timezone
import requests
import time
import datetime
import random
import hashlib
import _pdf2docx
import uuid
import _pytube
import _moviepy
import _PIL

app = Flask(__name__,template_folder="./_templates",static_folder="./_static")
CORS(app)
web_key = open("./config/web.key", 'r')
app.secret_key = str(web_key)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/converter')
def converter():
    return render_template("converter.html")

@app.route('/loader')
def loader():
    return render_template("loader.html")

@app.route('/convert/pdftodocx', methods=[ 'POST'])
def pdftodocx():
    files = request.files.getlist("file")
    for file in files:
        basename, extension = os.path.splitext(file.filename)
        tmp_file_name = str(uuid.uuid4())
        file.save("./tmp/"+tmp_file_name)
        _pdf2docx.convertPdfToDocx("./tmp/"+tmp_file_name,"./tmp/_"+tmp_file_name)
        os.remove("./tmp/"+tmp_file_name) 
        return send_file("./tmp/_"+tmp_file_name,download_name=basename+".docx",as_attachment=True), 200
    return "Error"

@app.route('/convert/pngtojpg', methods=[ 'POST'])
def pngtojpg():
    files = request.files.getlist("file")
    for file in files:
        basename, extension = os.path.splitext(file.filename)
        tmp_file_name = str(uuid.uuid4())
        file.save("./tmp/"+tmp_file_name)
        _PIL.convertImage("./tmp/"+tmp_file_name,"./tmp/_"+tmp_file_name,".jpg")
        os.remove("./tmp/"+tmp_file_name) 
        return send_file("./tmp/_"+tmp_file_name+".jpg",download_name=basename+".jpg",as_attachment=True), 200
    return "Error"

@app.route('/convert/jpgtopng', methods=[ 'POST'])
def jpgtopng():
    files = request.files.getlist("file")
    for file in files:
        basename, extension = os.path.splitext(file.filename)
        tmp_file_name = str(uuid.uuid4())
        file.save("./tmp/"+tmp_file_name)
        _PIL.convertImage("./tmp/"+tmp_file_name,"./tmp/_"+tmp_file_name,".png")
        os.remove("./tmp/"+tmp_file_name) 
        return send_file("./tmp/_"+tmp_file_name+".png",download_name=basename+".png",as_attachment=True), 200
    return "Error"
    
@app.route('/loader/mp4toyutube', methods=[ 'POST'])
def loaderyoutubemp4():
    link = request.form['link']
    tmp_file_name = str(uuid.uuid4())
    file_name = _pytube.Download(link,tmp_file_name)
    return send_file("./tmp/"+tmp_file_name,download_name=file_name+".mp4",as_attachment=True), 200

@app.route('/loader/yttomp3', methods=[ 'POST'])
def loaderyoutubemp3():
    link = request.form['link']
    tmp_file_name = str(uuid.uuid4())
    file_name = _pytube.Download(link,tmp_file_name)
    out = _moviepy.Convert("./tmp/"+file_name,tmp_file_name+".mp3")
    os.remove("./tmp/"+tmp_file_name)
    #return send_file(files,download_name=file_name+".mp3"), 200
    return send_file("./tmp/"+tmp_file_name+".mp3",download_name="325345",as_attachment=True), 200
    return send_file("./tmp/"+tmp_file_name+".mp3",download_name=file_name+".mp3",as_attachment=True), 200

        

def Genkey(name):
    gen = str(random.randint(8687685465675, 
    989898565675467324578789789))+str(random.randint(8687685465675, 
    989898219323478453177459789))+str(random.randint(8687685465675, 
    981231549309023747862389789))
    gen = bytes(gen, 'utf-8')
    gen = hashlib.sha256(gen).hexdigest()
    f = open(path+name, 'w')
    f.write(gen)
    f.close()


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "--new-key":
        Genkey("web.key")
        Genkey("ref.key")
        Genkey("ace.key")
        app.run(host=Conf["ip"], port=Conf['portweb'])
    if sys.argv[1] == "--start":
        app.run(host="0.0.0.0", port="1668")