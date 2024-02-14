import json
import sqlite3
import random
from flask import Flask, redirect, render_template, request, url_for


def nolasit_teksta_datus(vietnes_vieta):
  teksta_fails = open("Dati/teksti.json", encoding="utf8")
  vietnes_teksti = json.load(teksta_fails)
  teksta_fails.close()
  if vietnes_vieta == "sakums":
    return vietnes_teksti.get("sakums")
  elif vietnes_vieta == "registresanas":
    return vietnes_teksti.get("registresanas")
  elif vietnes_vieta == "ielogosanas":
    return vietnes_teksti.get("ielogosanas")
    

app = Flask("app")

@app.route("/")
def sakums():
  teksti = nolasit_teksta_datus("sakums")
  return render_template("sakums.html",teksti=teksti)

@app.route("/registresanas", methods=["GET", "POST"])
def registresanas():
  teksti = nolasit_teksta_datus("registresanas")
  return render_template("registresanas.html",teksti=teksti)
  
@app.route("/ielogosanas", methods=["GET", "POST"])
def ielogosanas():
  teksti = nolasit_teksta_datus("ielogosanas")
  return render_template("ielogosanas.html",teksti=teksti)
app.run(host="0.0.0.0", port=8080)