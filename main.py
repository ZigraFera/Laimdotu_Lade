import json
import sqlite3
import random
from flask import Flask, redirect, render_template, request, url_for
app = Flask("app")
@app.route("/")
def index():
  return render_template("sakums.html")
app.run(host="0.0.0.0", port=8080)