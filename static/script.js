let epasts = document.getElementById("epasts");
let paroles_mainosais_epasts = document.getElementById("epasts1");
let lvards = document.getElementById("lvards");
let epasta_kluda = document.getElementById("epasta_kluda");
let lvards_kluda = document.getElementById("lvards_kluda");
let j_parole = document.getElementById("j_parole");
let apstiprinajums = document.getElementById("apstiprinajums");
let apstiprinajums_kluda = document.getElementById("apstiprinajums_kluda");
let elements = document.getElementById("animacija");
let registret = false;
let ielogot = false;
const Lietotajvardi = [];
const Pasti = [];




function EpastaParbaude() {
  if (epasts.value != "") {
    if (!epasts.value.match(/^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {
      epasta_kluda.innerHTML = "e-pasts nav derīgs!";
      epasts.style.borderColor = "red";
      return false;
    }
    epasta_kluda.innerHTML = "";
    epasts.style.borderColor = "#ecb154";
    return true;
  }
  epasta_kluda.innerHTML = "";
  epasts.style.borderColor = "#ecb154";

}




function ParolesSakritiba() {
  if (j_parole.value != "" && apstiprinajums.value != "") {
    if (j_parole.value != apstiprinajums.value) {
      apstiprinajums_kluda.innerHTML = "Paroles nesakrīt!";
      apstiprinajums.style.borderColor = "red";
      j_parole.style.borderColor = "red";
      return false;
    }
    apstiprinajums_kluda.innerHTML = "";
    apstiprinajums.style.borderColor = "#ecb154";
    j_parole.style.borderColor = "#ecb154";
    return true;
  }
  apstiprinajums_kluda.innerHTML = "";
  apstiprinajums.style.borderColor = "#ecb154";
  j_parole.style.borderColor = "#ecb154";
}

function VistokluAnimacija(clicked_id) {

  if (clicked_id == "varianti1") {
    registret = true;
    elements.classList.add("Vistoklis");
  }
  if (clicked_id == "varianti2") {
    ielogot = true;
    elements.classList.add("Vistoklis2");
  }
  elements.addEventListener("animationend", AnimacijaBeidzas);
  elements.addEventListener("animationstart", AnimacijaSakas);
}

function SleptPogas() {
  document.getElementById("varianti1").style.visibility = "hidden";
  document.getElementById("varianti2").style.visibility = "hidden";
}

function RaditPogas() {
  document.getElementById("varianti1").style.visibility = "visible";
  document.getElementById("varianti2").style.visibility = "visible";
}

function AnimacijaSakas() {
  SleptPogas();
}

function AnimacijaBeidzas() {

  Parslegsanas();
  RaditPogas();
}

function Bridinat() {
  if (confirm("Ja anulēsi kontu zaudēsi savus darbus! Lejuplādējiet failus pirms anulēšanas! Vai vēl joprojām vēlaties anulēt kontu?")) {
    Aptauja();
  } else {
    alert("Konta anulēšana atcelta!");
  }
}

function Parslegsanas() {
  document.body.classList.add("fade-out");

  setTimeout(function () {
    document.body.classList.add("fade-in");
    if (registret == true) {
      window.location.href = "/registresanas";
    } else if (ielogot == true) {
      window.location.href = "/ielogosanas";
    }
  }, 1000);
}
function Aptauja() {
  const aptauja = document.getElementById("aptauja");
  const parklajs = document.getElementById("parklaj"); // iegūst elementu
  aptauja.classList.add("active"); //pivieno klasi
  parklajs.classList.add("active");
}
function Apstiprinat(){
  const aptauja = document.getElementById("aptauja");
  const parklajs = document.getElementById("parklaj");
  aptauja.classList.remove("active"); // pievieno klasi
  parklajs.classList.remove("active");
  win.location.href = "/anulet_kontu";
}
function Noliegt() {
  const aptauja = document.getElementById("aptauja");
  const parklajs = document.getElementById("parklaj");
  aptauja.classList.remove("active"); // pievieno klasi
  parklajs.classList.remove("active");
}
function ParaditAprakstu(){
  let drosibasTipsSelect = document.getElementById("drosibas_tips").selectedIndex;
 
  switch(drosibasTipsSelect){
    case 0:
      document.getElementById("apraksts").innerHTML= "";
      break;
    case 1:
      document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips1").value;
      break;
    case 2:
      document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips2").value;
      break;
      case 3:
      document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips3").value;
      break;
  }
  // let paskaidrojumsElements = document.querySelectorAll(".Paskaidrojums");

  // // paslēp paskaidrojumus
  // paskaidrojumsElements.forEach(function (element) {
  //     element.style.display = "none";
  // });

  // // parāda paskaidrojumu, atbilstoši izvēlētajam drošibas tipam
  // let selectedDrosibasTips = drosibasTipsSelect.value;
  // let selectedPaskaidrojumaElements = document.getElementById(`paskaidrojums-${selectedDrosibasTips}`);
  // if (selectedPaskaidrojumaElements) {
  //     selectedPaskaidrojumaElements.style.display = "block";
  // }
}
function IedarbinatLietotajs(){
  let konkretsLietotajsCheckbox = document.getElementById("konkrets_lietotajs");
  let lietotajsSelect = document.getElementById("lietotajs_izvele");
  if(!konkretsLietotajsCheckbox.checked){
    lietotajsSelect.disabled = true;
  }
  else{
    lietotajsSelect.disabled = false;
  }
 
}
