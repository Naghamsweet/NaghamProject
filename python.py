from ast import Return
from sqlite3 import Cursor, connect
from flask import Flask, render_template, request, flash, abort, current_app, make_response

from mimetypes import guess_extension
from werkzeug.utils import secure_filename
from gtts import gTTS
from flask import jsonify
import os
from playsound import playsound
from os import path
import webbrowser 
import speech_recognition as sr
import pymysql







app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
  
 return render_template("javahtml.html")
  
@app.route("/info", methods=['POST'])
def info():
        username=request.form.get("uname")
        password=request.form.get("psw")
        connection=pymysql.connect(host="localhost",user="root",passwd="123456",database="pythondb")
        Cursor=connection.cursor()
        q="INSERT INTO USERS(user_pass,user_name)VALUES(%s,%s)"
        v=(password,username)  
        Cursor.execute(q,v)
        f="Select * from  users;"
        Cursor.execute(f)
        rows=Cursor.fetchall()
        for row in rows:
           print(row)
        connection.commit()
        connection.close()
        return render_template("javahtml2.html",first_name=username, last_name=password)
	    
@app.route("/back",methods=["POST"])
def o():
        return render_template("javahtml.html")


if __name__=="__main__":
     app.run(port=7000)