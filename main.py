import json
import os
import sqlite3
from io import BytesIO
import shutil
from flask import Flask, redirect, render_template, request, url_for, send_from_directory, send_file, make_response
from werkzeug.utils import secure_filename





def update_sql(cmd, value=None):
  savienojums = sqlite3.connect('lietotaji.db')
  s = savienojums.cursor()

  if value is not None:
    res = s.execute(cmd, value).fetchall()
  else:
    res = s.execute(cmd).fetchall()

  savienojums.commit()
  savienojums.close()
  return res


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
  lietotajvards VARCHAR(100) PRIMARY KEY NOT NULL,\
  vards TEXT NOT NULL,\
  uzvards TEXT NOT NULL,\
  pasts VARCHAR(200) NOT NULL UNIQUE,\
  parole VARCHAR(50) NOT NULL,\
  darbi INTEGER DEFAULT 0)")

select_sql("CREATE TABLE IF NOT EXISTS Darbs (\
  darbs_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
  autors VARCHAR(100),\
  nosaukums VARCHAR(200),\
  piekluves_nosaukums TEXT,\
  konkrets_lietotajs BOOL,\
  lietotaji TEXT,\
  redzams BOOL,\
  ladejams BOOL,\
  dati BLOB, \
  faila_adrese TEXT,\
  FOREIGN KEY(piekluves_nosaukums) REFERENCES Piekluves(piekluves_nosaukums),\
  FOREIGN KEY(autors) REFERENCES Konts(lietotajvards))")

select_sql("CREATE TABLE IF NOT EXISTS Piekluves (\
  piekluves_nosaukums TEXT PRIMARY KEY,\
  apraksts TEXT,\
  redzams BOOL,\
  ladejams BOOL,\
  konkrets_lietotajs BOOL)")

insert_sql("INSERT OR IGNORE INTO Piekluves (\
   piekluves_nosaukums,apraksts,redzams,ladejams,konkrets_lietotajs) \
  VALUES ('Ieslēgts lādē','Neviens cits nevar rdzēt vai lejupielādēt šo darbu', false,false,false),\
        ('Atklāts','Visi redz, un var lejupladet šo darbu', true,true,false),\
        ('Uzticēta atslega','Darba piekļuves atļaujas piešķir pēc saviem ieskatiem, konkrētām personām','','',true)"
        )

# ('Uzticēta atslega','Darba piekļuves atļaujas piešķir pēc saviem ieskatiem, konkrētām personām','','',true),\
# select_sql("CREATE TABLE IF NOT EXISTS Konts (\
#   konts_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
#   lietotajvards VARCHAR(50) NOT NULL UNIQUE,\
#   vards TEXT NOT NULL,\
#   uzvards TEXT NOT NULL,\
#   pasts VARCHAR(200) NOT NULL UNIQUE,\
#   parole VARCHAR(50) NOT NULL,\
#   darbi INTEGER DEFAULT 0)")
# #autors bija Varchar saistīts ar lietotajvardu, bet tagad Intager, eskperiments
# select_sql("CREATE TABLE IF NOT EXISTS Darbs (\
#   darbs_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
#   autors INTEGER,\
#   nosaukums VARCHAR(200),\
#   piekluves_nosaukums TEXT,\
#   konkrets_lietotajs BOOL,\
#   lietotaji TEXT,\
#   redzams BOOL,\
#   ladejams BOOL,\
#   dati BLOB, \
#   faila_adrese TEXT,\
#   FOREIGN KEY(piekluves_nosaukums) REFERENCES Piekluves(piekluves_nosaukums),\
#   FOREIGN KEY(autors) REFERENCES Konts(konts_ID))")

# select_sql("CREATE TABLE IF NOT EXISTS Piekluves (\
#   piekluves_nosaukums TEXT PRIMARY KEY,\
#   apraksts TEXT,\
#   redzams BOOL,\
#   ladejams BOOL,\
#   konkrets_lietotajs BOOL)")

# insert_sql("INSERT OR IGNORE INTO Piekluves (\
#    piekluves_nosaukums,apraksts,redzams,ladejams,konkrets_lietotajs) \
#   VALUES ('Ieslēgts lādē','Neviens cits nevar rdzēt vai lejupielādēt šo darbu', false,false,false),\
#         ('Atklāts','Visi redz, un var lejupladet šo darbu', true,true,false),\
#         ('Uzticēta atslega','Darba piekļuves atļaujas piešķir pēc saviem ieskatiem, konkrētām personām','','',true)"
#         )

# ('Uzticēta atslega','Darba piekļuves atļaujas piešķir pēc saviem ieskatiem, konkrētām personām','','',true),\


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


def IzveidotLietotajaMapi(konts):
  main_folder = os.path.join("Augsuplades", str(konts))
  public_folder = os.path.join(main_folder, "public")
  private_folder = os.path.join(main_folder, "private")

  if not os.path.exists(main_folder):
    os.makedirs(main_folder)
  if not os.path.exists(public_folder):
    os.makedirs(public_folder)
  if not os.path.exists(private_folder):
    os.makedirs(private_folder)

  return main_folder, public_folder, private_folder


def find_file_location(darbs_ID, file):


  file_data = select_sql2(
      "SELECT autors, nosaukums,redzams,ladejams FROM Darbs WHERE darbs_ID = ?",
      (darbs_ID, ))
  autors, nosaukums, redzams, ladejams = file_data[0]
  konts = select_sql2("SELECT konts_ID FROM Konts WHERE lietotajvards=?",
                      (autors, ))
  main_folder = os.path.join("Augsuplades", str(konts[0][0]))
  public_folder = os.path.join(main_folder, "public", file)
  private_folder = os.path.join(main_folder, "private", file)
  if file_data[0][2] == "true" and file_data[0][3] == "true":
    file_location = public_folder
  else:
    file_location = private_folder
  return file_location


app = Flask("app")

app.config['ALLOWED_EXTENSIONS'] = [
    '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.doc', '.docx', '.xls', '.xlsx',
    '.ppt', '.pptx', '.mp4', '.mp3', 'm4a', '.wav', '.ogg'
]


@app.route("/")
def sakums():
  global public_path, private_path
  teksti = nolasit_teksta_datus("sakums")
  teksti2 = nolasit_teksta_datus("vide")

  konts = request.cookies.get("konts")
  lietotajs = request.cookies.get("lietotajs")
  if konts is not None:
    darbi_skaits = select_sql2("SELECT COUNT(darbs_ID) FROM Darbs WHERE autors = ?",
                        (lietotajs, ))[0]
    darbi= darbi_skaits[0]
    lietotaja_darbi = update_sql("UPDATE Konts SET darbi = ? WHERE konts_ID = ?",	(darbi, konts))
    
    saraksts = select_sql2("SELECT konts_ID, lietotajvards, pasts FROM Konts")
    info = insert_sql(
        "SELECT lietotajvards, pasts, darbi, konts_ID FROM Konts WHERE konts_ID = ?",
        (konts, ))[0]
    

   
    privatais_darbu_saraksts = select_sql2(
        "SELECT darbs_ID, autors, nosaukums, redzams, ladejams,faila_adrese FROM Darbs  WHERE autors = ? AND redzams = 'false'AND ladejams = 'false'",
        (lietotajs, ))
    publiskais_darbu_saraksts = select_sql2(
        "SELECT darbs_ID, autors, nosaukums, redzams, ladejams, faila_adrese FROM Darbs  WHERE redzams = 'true'AND ladejams = 'true'"
    )
    # autors = info[3]
    main_folder, public_folder, private_folder = IzveidotLietotajaMapi(konts)
    print(f"user_folder: {main_folder}")
    print(f"public_folder: {public_folder}")
    print(f"private_folder: {private_folder}")
    print(f"private_folder: {private_folder}")
    
    print("Info:", info)
    print("Darbu_saraksts (privātie darbi):", privatais_darbu_saraksts)
    print("Darbu_saraksts (darbi):", darbi)
    print("Darbu_saraksts (publiskie darbi):", publiskais_darbu_saraksts)

    return render_template("vide.html",
                           teksti2=teksti2,
                           info=info,
                           saraksts=saraksts,
                           privatais_darbu_saraksts=privatais_darbu_saraksts,
                           publiskais_darbu_saraksts=publiskais_darbu_saraksts,
                          lietotajs=lietotajs
                           # konts=konts,
                           # autors=autors,
                         )
  return render_template("sakums.html", teksti=teksti)


@app.route("/paroles_maina", methods=["POST", "GET"])
def paroles_maina():
  teksti = nolasit_teksta_datus("paroles_maina")
  if request.method == "POST":

    konts = request.cookies.get("konts")

    update_sql("UPDATE Konts SET parole=? WHERE pasts = ?",
               (request.form['j_parole'], request.form['epasts1']))
    redirect("/ielogosanas")
  return render_template("paroles_maina.html", teksti=teksti)


@app.route("/registresanas", methods=["GET", "POST"])
def registresanas():
  kluda = ""
  teksti = nolasit_teksta_datus("registresanas")
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
      return render_template("registresanas.html", teksti=teksti, kluda=kluda)

  return render_template("registresanas.html", teksti=teksti)


@app.route("/ielogosanas", methods=["GET", "POST"])
def ielogosanas():
  kluda = ""
  teksti = nolasit_teksta_datus("ielogosanas")
  if request.method == "POST":
    answer_rezult = select_sql2("SELECT konts_ID,lietotajvards FROM Konts WHERE lietotajvards = ? AND parole = ?",\
                        (request.form["lvards"], request.form["parole"], ))
    if len(answer_rezult) > 0:
      answer = redirect("/")
      answer.set_cookie("konts", str(answer_rezult[0][0]))
      answer.set_cookie('lietotajs', str(answer_rezult[0][1]))

      return answer
    else:
      kluda = "Nepareizs lietotājvārds vai parole"

  return render_template("ielogosanas.html", teksti=teksti, kluda=kluda)


@app.route("/izlogoties")
def izlogoties():
  answer = redirect("/")
  answer.delete_cookie("konts")
  answer.delete_cookie("lietotajs")
  return answer


@app.route("/jauns_darbs", methods=["GET", "POST"])
def jauns_darbs():
  piekluves = select_sql(
      "SELECT piekluves_nosaukums,apraksts,redzams,ladejams FROM Piekluves")
  lietotaji = select_sql("SELECT lietotajvards, pasts FROM Konts")
 
  # public_folder = os.path.join(main_folder, "public")
  # private_folder = os.path.join(main_folder, "private")
  # if not os.path.exists(public_folder):
  #   os.makedirs(public_folder)
  # if not os.path.exists(private_folder):
  #   os.makedirs(private_folder)

  # print(f"user_folder: {main_folder}")
  # print(f"public_folder: {public_folder}")
  # print(f"private_folder: {private_folder}")

 


  return render_template("jauns_darbs.html",
                         piekluves=piekluves,
                         lietotaji=lietotaji)


@app.route("/darba_ievietosana", methods=["POST"])
def darba_ievitosana():
  fails = request.files["darba_fails"]
  tips = os.path.splitext(fails.filename)[1]
  if tips not in ['.jpg', '.jpeg', '.png', '.gif']:
    return "Failam nav piņemams formāts. Lūdzu izvēlieties citu failu."
  konts = request.cookies.get("konts")
  autors = select_sql2("SELECT lietotajvards FROM Konts WHERE konts_ID = ?",
                       (konts, ))[0][0]
  drosibas_tips = request.form['drosibas_tips']
  redzams = request.form['redzams_1']
  ladejamiba = request.form['ladejams_1']
  # print(f"autors: {autors}")

 
  main_folder, public_folder, private_folder = IzveidotLietotajaMapi(konts)
  if redzams == "true" and ladejamiba == "true":
    folder_path = public_folder
  else:
    folder_path = private_folder

  # Saglabāt failu
  fails.save(os.path.join(folder_path, secure_filename(fails.filename)))
  faila_adrese = os.path.join(folder_path, secure_filename(fails.filename))

  # konkrets_lietotajs = request.form['konkrets_lietotajs']
  # izveletais = request.form['lietotajs_izvele'] if konkrets_lietotajs == 'true' else None
  answer = insert_sql(
      "INSERT INTO Darbs(autors, nosaukums, piekluves_nosaukums, redzams, ladejams, dati,faila_adrese) "
      "VALUES (?, ?, ?, ?, ?, ?,?)",
      (autors, fails.filename, drosibas_tips, redzams, ladejamiba,
       fails.read(), faila_adrese))

 
  return redirect('/')




#dzeš darbu


@app.route('/dzest_darbs/<int:darbs_ID>', methods=["POST"])
def dzest_darbs(darbs_ID):
  konts = request.cookies.get("konts")

  
  autors = select_sql2("SELECT lietotajvards FROM Konts WHERE konts_ID = ?",
                       (konts, ))[0][0]

  if autors:
    
    file_data = select_sql2(
        "SELECT nosaukums, redzams, ladejams, dati FROM Darbs WHERE darbs_ID = ?",
        (darbs_ID, ))

    
    delete_sql("DELETE FROM Darbs WHERE darbs_ID=?", (darbs_ID, ))

    
    main_folder, public_folder, private_folder = IzveidotLietotajaMapi(konts)
    if file_data[0][1] == "true" and file_data[0][2] == "true":
      folder_path = public_folder
    else:
      folder_path = private_folder

    file_path = os.path.join(
        folder_path,
        file_data[0][0])  

    if os.path.exists(file_path):
      os.remove(file_path)

    return redirect('/')
  else:
    
    return "Neatļauta piekļuve", 403


@app.route('/skatit_darbs/<int:darbs_ID>', methods=["GET"])
def skatit_darbs(darbs_ID):
  konts = request.cookies.get("konts")
  lietotajs = request.cookies.get("lietotajs")
  fails = select_sql2(
      "SELECT autors, nosaukums, faila_adrese, redzams FROM Darbs WHERE darbs_ID = ?",
      (darbs_ID, ))
  if fails:
    autors = fails[0][0]
    file_name = fails[0][1]
    file_location = fails[0][2]
    redzams = fails[0][3]

    if redzams == 'true' or autors == lietotajs:
      # print(f"Autors:{autors}: konts:{konts}" ) ar otro datu bāze principu atpazīst bet neredz failu
      if os.path.exists(file_location):
       
        file_extension = os.path.splitext(file_name)[1].lower()
      

       
        # if file_extension in ['.mp4', '.webm', '.ogg','.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
        #   # Dokumenta,Video, Audio fails
        #   return render_template('view.html', file_location=file_location)
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
          # Bildes fails
          return send_file(file_location, as_attachment=False)
       
        else:
      
          return "Neatbalstīts faila tips", 400
      else:
        
        return "fails nav atrasts", 404
    else:
      
      return "Fails nav redzams", 403
  else:
    
    return "Faila informācija nav atrasta", 404


@app.route('/ladet_darbs/<int:darbs_ID>', methods=["GET"])
def ladet_darbs(darbs_ID):
  konts = request.cookies.get("konts")
  fails = select_sql2(
      "SELECT nosaukums, faila_adrese FROM Darbs WHERE darbs_ID = ?",
      (darbs_ID, ))
  if fails:
    file_name = fails[0][0]
    file_location = fails[0][1]

    if os.path.exists(file_location):
      return send_file(file_location, as_attachment=True)
    else:
      return "File not found", 404
  else:
    return "File information not found", 404
  

def DzestLietotajaMapi(konts):
  main_folder = os.path.join("Augsuplades", str(konts))
  # Delete the folder and its contents
  shutil.rmtree(main_folder, ignore_errors=True)
  print(f"Folder '{main_folder}' and its contents have been deleted.")
#dzeš kontu
@app.route('/anulet_kontu', methods=["POST", "GET"])
def anulet_konts():
  if request.method == "POST":
    konts = request.cookies.get("konts")
    lietotajs = request.cookies.get("lietotajs")
    answer_rezult = select_sql2("SELECT konts_ID FROM Konts WHERE parole = ?", (request.form["parole_dzes"],))
    if len(answer_rezult) > 0:
        # Delete the user's account and associated folder
        delete_sql("DELETE FROM Darbs WHERE autors = ?", (lietotajs,))
        delete_sql("DELETE FROM Konts WHERE konts_ID = ?", (konts,))
        DzestLietotajaMapi(konts)
        # Logout the user
        return redirect('/izlogoties')
    
  return redirect('/')
  
app.run(host="0.0.0.0", port=8080, debug=True)
