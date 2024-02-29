import json
import sqlite3
from flask import Flask, redirect, render_template, request, url_for


def delete_sql(cmd, value=None):
  savienojums = sqlite3.connect('lietotaji.db')
  s = savienojums.cursor()

  if value is not None:
    res = s.execute(cmd, value).fetchall()
  else:
    res = s.execute(cmd).fetchall()

  savienojums.commit()
  savienojums.close()
  return res


def insert_sql(cmd, value=None):
  savienojums = sqlite3.connect("lietotaji.db")
  s = savienojums.cursor()

  if value is not None:
    answer = s.execute(cmd, value).fetchall()
  else:
    answer = s.execute(cmd).fetchall()

  savienojums.commit()
  savienojums.close()
  return answer


def select_sql(cmd):
  savienojums = sqlite3.connect("lietotaji.db")
  s = savienojums.cursor()
  answer = s.execute(cmd).fetchall()
  savienojums.commit()
  savienojums.close()
  return answer


def select_sql2(cmd, value=None):
  savienojums = sqlite3.connect("lietotaji.db")
  s = savienojums.cursor()

  if value is not None:
    answer = s.execute(cmd, value).fetchall()
  else:
    answer = s.execute(cmd).fetchall()

  savienojums.commit()
  savienojums.close()
  return answer


select_sql("CREATE TABLE IF NOT EXISTS Konts (\
  konts_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
  lietotajvards VARCHAR(50) NOT NULL UNIQUE,\
  vards TEXT NOT NULL,\
  uzvards TEXT NOT NULL,\
  pasts VARCHAR(200) NOT NULL UNIQUE,\
  parole VARCHAR(50) NOT NULL,\
  darbi INTEGER DEFAULT 0)")

select_sql("CREATE TABLE IF NOT EXISTS Darbs (\
  darbs_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
  konts_ID INTEGER,\
  nosaukums VARCHAR(200),\
  piekluves_nosaukums TEXT,\
  konkrets_lietotajs BOOL,\
  redzams BOOL,\
  ladejams BOOL,\
  dati BLOB, \
  FOREIGN KEY(piekluves_nosaukums) REFERENCES Piekluves(piekluves_nosaukums)\
  FOREIGN KEY(konts_ID) REFERENCES Konts(konts_ID))")

select_sql("CREATE TABLE IF NOT EXISTS Piekluves (\
  piekluves_nosaukums TEXT PRIMARY KEY,\
  apraksts TEXT,\
  redzams BOOL,\
  ladejams BOOL,\
  konkrets_lietotajs BOOL)")

insert_sql("INSERT OR IGNORE INTO Piekluves (\
   piekluves_nosaukums,apraksts,redzams,ladejams,konkrets_lietotajs) \
  VALUES ('Ieslēgts lādē','Neviens cits nevar rdzēt vai lejupielādēt šo darbu', false,false,false),\
         ('Uzticēta atslega','Darba piekļuves atļaujas piešķir pēc saviem ieskatiem, konkrētām personām','','',true),\
         ('Atklats','Visi redz, un var lejupladet šo darbu', true,true,false)")


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
  elif vietnes_vieta == "paroles_maina":
    return vietnes_teksti.get("paroles_maina")
  elif vietnes_vieta == "vide":
    return vietnes_teksti.get("vide")


app = Flask("app")


@app.route("/")
def sakums():
  teksti = nolasit_teksta_datus("sakums")
  teksti2 = nolasit_teksta_datus("vide")

  konts = request.cookies.get("konts")

  if konts is not None:

    info = insert_sql(
        "SELECT lietotajvards, pasts, darbi, \
      konts_ID FROM Konts WHERE Konts_id = ?", (konts, ))[0]
    saraksts = select_sql2(
        "SELECT konts_ID, lietotajvards,pasts FROM Konts WHERE konts_ID = ?",
        (konts, ))
    darbu_saraksts = select_sql2(
        "SELECT konts_ID, nosaukums, redzams, ladejams FROM Darbs WHERE konts_ID = ? AND (redzams = true OR konkrets_lietotajs = true)",
      
        (konts, ))

    return render_template("vide.html",
                           teksti2=teksti2,
                           info=info,
                           saraksts=saraksts,
                           darbu_saraksts=darbu_saraksts)
  return render_template("sakums.html", teksti=teksti)


# @app.route("/vide")
# def vide():
#   teksti2 = nolasit_teksta_datus("vide")
#   return render_template("vide.html", teksti2=teksti2)


@app.route("/registresanas", methods=["GET", "POST"])
def registresanas():
  kluda = ""
  teksti = nolasit_teksta_datus("registresanas")
  # dati = select_sql("SELECT * FROM Konts")
  # lvardi = select_sql("SELECT lietotajvards FROM Konts")
  # pasti = select_sql("SELECT pasts FROM Konts")
  if request.method == "POST":
    
    answer= select_sql2("SELECT lietotajvards FROM Konts WHERE lietotajvards = ?",\
                       (request.form["lvards"],))

    print(answer)
    if len(answer) == 0:
      insert_sql("INSERT INTO Konts(lietotajvards,vards,uzvards,pasts,parole) VALUES (?, ?,?,?,?)",\
                 (request.form["lvards"],request.form["vards"],request.form["uzvards"],request.form["epasts"], request.form["parole"] ))
      
      return redirect("/ielogosanas")
    else:
      kluda = "Lietotājvārds jau eksistē"
      return render_template("registresanas.html", teksti=teksti,kluda=kluda)

 


  return render_template("registresanas.html", teksti=teksti)


@app.route("/ielogosanas", methods=["GET", "POST"])
def ielogosanas():
  teksti = nolasit_teksta_datus("ielogosanas")
  if request.method == "POST":
    answer_rezult = select_sql2("SELECT konts_ID FROM Konts WHERE lietotajvards = ? AND parole = ?",\
                        (request.form["lvards"], request.form["parole"], ))
    if len(answer_rezult) > 0:
      answer = redirect("/")
      answer.set_cookie("konts", str(answer_rezult[0][0]))
      return answer

  return render_template("ielogosanas.html", teksti=teksti)


@app.route("/izlogoties")
def izlogoties():
  answer = redirect("/")
  answer.delete_cookie("konts")
  return answer


@app.route("/jauns_darbs", methods=["GET", "POST"])
def jauns_darbs():
  piekluves = select_sql("SELECT piekluves_nosaukums,apraksts FROM Piekluves")
  lietotaji = select_sql("SELECT lietotajvards, pasts FROM Konts")

  return render_template("jauns_darbs.html",
                         piekluves=piekluves,
                         lietotaji=lietotaji)


@app.route("/darba_ievietosana", methods=["GET", "POST"])
def jauns_darbs():
  if request.method == "POST":

    darba_fails = request.files["file"]
    darbs = insert_sql("INSERT INTO Darbs(konts_ID,nosaukums,piekluves,konkrets_lietotajs,redzams,ladejams) VALUES (?,?,?,?,?,?)")

  return render_template("jauns_darbs.html",teksti2=teksti2)

# @app.route("/lejuplade/<darbs_ID>", methods=["GET", "POST"])
# def lejuplade(darbs_ID):

#dzeš darbu


@app.route('/dzest_trenins/<int:darbs_ID>', methods=["POST"])
def dzest_trenins(darbs_ID):
  delete_sql("DELETE FROM Darbs WHERE darbs_ID=?", (darbs_ID, ))
  return redirect('/')


#dzeš kontu
@app.route('/anulet_kontu', methods=["POST", "GET"])
def dzest_konts():
  if request.method == "POST":
    konts = request.cookies.get("konts")
    answer_rezult = insert_sql("SELECT konts_ID FROM Konts WHERE parole = ?",\
                               (request.form["parole_dzes"], ))
    if len(answer_rezult) > 0:
        delete_sql(f"DELETE FROM Darbs WHERE konts_ID = {konts}")
        delete_sql("DELETE FROM Konts WHERE konts_ID = ?", (konts, ))

    

  return redirect('/')


app.run(host="0.0.0.0", port=8080)
