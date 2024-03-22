let epasts = document.getElementById("epasts");
let paroles_mainosais_epasts = document.getElementById("epasts1");
let lvards = document.getElementById("lvards");
let epasta_kluda = document.getElementById("epasta_kluda");
let lvards_kluda = document.getElementById("lvards_kluda");
let j_parole = document.getElementById("j_parole");
let apstiprinajums = document.getElementById("apstiprinajums");
let apstiprinajums_kluda = document.getElementById("apstiprinajums_kluda");
let elements = document.getElementById("animacija");
let redzlab = document.getElementById("r");
let sleplab = document.getElementById("s");
let ladejlab = document.getElementById("l");
let neladejlab = document.getElementById("nl");
let konk = document.getElementById("konkrets");
let izv = document.getElementById("izv");
let ele = document.getElementsByName("redz");
let registret = false;
let ielogot = false;



// Pārbauda e-pastu

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
// Pārbauda jaunās paroles apstiprinājumu
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
//Animācija un elementu kotrole
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
//Anulēšanas vrīdinājums
function Bridinat() {
  if (confirm("Ja anulēsi kontu zaudēsi savus darbus! Lejuplādējiet failus pirms anulēšanas! Vai vēl joprojām vēlaties anulēt kontu?")) {
    Aptauja();
  } else {
    alert("Konta anulēšana atcelta!");
  }
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
}
function Noliegt() {
  const aptauja = document.getElementById("aptauja");
  const parklajs = document.getElementById("parklaj");
  aptauja.classList.remove("active"); // pievieno klasi
  parklajs.classList.remove("active");
}
function JaunaDarbaStadija(){
  let konkretsLietotajsCheckbox = document.getElementById("konkrets_lietotajs");
  let lietotajsSelect = document.getElementById("lietotajs_izvele");
  let redzamiba = document.getElementById("redzams")
  let slepts = document.getElementById("slepts")
  let ladejams = document.getElementById("lade")
  let neladejams = document.getElementById("nelade")
  redzlab.style.display = "none";
  redzamiba.style.visibility = "hidden";
  sleplab.style.display = "none";
  slepts.style.visibility = "hidden";
  ladejlab.style.display = "none";
  ladejams.style.visibility = "hidden";
  neladejams.style.display = "none";
  neladejlab.style.visibility = "hidden";
  // konk.style.display = "none";
  // konkretsLietotajsCheckbox.style.visibility = "hidden";
  // izv.style.display = "none";
  // lietotajsSelect.style.visibility = "hidden";
  document.getElementById("redzams_1").value = ""
  
}
//Darba iestatījumu kontrole
function ParaditAprakstu(){
  let drosibasTipsSelect = document.getElementById("drosibas_tips").selectedIndex;
  let konkretsLietotajsCheckbox = document.getElementById("konkrets_lietotajs");
  let lietotajsSelect = document.getElementById("lietotajs_izvele");
  let redzamiba = document.getElementById("redzams");
  let slepts = document.getElementById("slepts");
  let ladejams = document.getElementById("lade");
  let neladejams = document.getElementById("nelade");
  
  document.getElementById("redzams_1").value = "";
  
  
  switch(drosibasTipsSelect){
      
    case 0:
      for(let i=0;i<ele.length;i++)
        ele[i].checked = false;
      document.getElementById("redzams_1").value = "";
      document.getElementById("ladejams_1").value = "";
      redzlab.style.display = "none";
      redzamiba.style.visibility = "hidden";
      sleplab.style.display = "none";
      slepts.style.visibility = "hidden";
      ladejlab.style.display = "none";
      ladejams.style.visibility = "hidden";
      neladejams.style.display = "none";
      neladejlab.style.visibility = "hidden";
      konk.style.display = "none";
      konkretsLietotajsCheckbox.style.visibility = "hidden";
      izv.style.display = "none";
      lietotajsSelect.style.visibility = "hidden";  
      document.getElementById("apraksts").innerHTML= "";
      break;
      
    case 1:
      document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips1").value;
      slepts.checked = true;
      neladejams.checked = true;
      redzlab.style.display = "none";
      redzamiba.style.visibility = "hidden";
      sleplab.style.display = "";
      slepts.style.visibility = "visible";
      ladejlab.style.display = "none";
      ladejams.style.visibility = "hidden";
      neladejams.style.display = "";
      neladejlab.style.visibility = "visible";
      // konk.style.display = "none";
      // konkretsLietotajsCheckbox.style.visibility = "hidden";
      // izv.style.display = "none";
      // lietotajsSelect.style.visibility = "hidden";
      document.getElementById("redzams_1").value = "false";
      document.getElementById("ladejams_1").value = "false";
      
      // if (document.getElementById("redzams_1").value== "true") {
      //   console.log("Selected: Redzams");
      //   // Additional logic if Redzams is selected
      // } else if (document.getElementById("redzams_1").value== "false") {
      //   console.log("Selected: Neredzams");
      //   // Additional logic if Neredzams is selected
      // }
      // else{
      //   console.log("Selected: none");
      // }
      break;
    case 2:
      
      redzamiba.checked = true;
      ladejams.checked = true;
      redzlab.style.display = "";
      redzamiba.style.visibility = "visible";
      sleplab.style.display = "none";
      slepts.style.visibility = "hidden";
      ladejlab.style.display = "";
      ladejams.style.visibility = "visible";
      neladejams.style.display = "none";
      neladejlab.style.visibility = "hidden";
      //konk.style.display = "none";
      //konkretsLietotajsCheckbox.style.visibility = "hidden";
      //izv.style.display = "none";
      //lietotajsSelect.style.visibility = "hidden";
      document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips2").value;
      if (document.getElementById("redzams_1").value== "true") {
        console.log("Selected: Redzams");
      } else if (document.getElementById("redzams_1").value== "false") {
        console.log("Selected: Neredzams");
        
      }
      else{
        console.log("Selected: none");
      }
      break;
      // case 3: 
        // document.getElementById("redzams_1").value = "";
        // document.getElementById("ladejams_1").value = "";
        // document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips2").value;
  
        // if(document.getElementById("redzams_1").value== "" && document.getElementById("ladejams_1").value== "")
        //   slepts.chacked = "false";
        //   redzamiba.chacked = "false";
        //   ladejams.chacked = "false";
        //   neladejams.chacked = "false";
        // redzlab.style.display = "";
        // redzamiba.style.visibility = "visible";
        // sleplab.style.display = "";
        // slepts.style.visibility = "visible";
        // ladejlab.style.display = "";
        // ladejams.style.visibility = "visible";
        // neladejams.style.display = "";
        // neladejlab.style.visibility = "visible";
        // konk.style.display = "";
        // konkretsLietotajsCheckbox.style.visibility = "visible";
        // izv.style.display = "";
        // lietotajsSelect.style.visibility = "visible";
      //   redzlab.style.display = "";
      //   redzamiba.style.visibility = "visible";
      //   sleplab.style.display = "none";
      //   slepts.style.visibility = "hidden";
      //   ladejlab.style.display = "";
      //   ladejams.style.visibility = "visible";
      //   neladejams.style.display = "none";
      //   neladejlab.style.visibility = "hidden";
      //   konk.style.display = "none";
      //   konkretsLietotajsCheckbox.style.visibility = "hidden";
      //   izv.style.display = "none";
      //   lietotajsSelect.style.visibility = "hidden";
      //   document.getElementById("apraksts").innerHTML= document.getElementById("drosiba_tips3").value;
      //   if (redzamiba.chacked == true&&slepts.chacked == false) {
      //     console.log("Selected: Redzams");
      //     document.getElementById("redzams_1").value = "true";
      //   }
      //   else if (slepts.chacked == true && redzamiba.chacked == false){
      //     console.log("Selected: neredzams");
      //     document.getElementById("redzams_1").value = "false";
      //   }
      //   if (ladejams.chacked == ladejams&&neladejams.chacked == false) {
      //     console.log("Selected: Redzams");
      //     document.getElementById("ladejams_1").value = "true";
      //   }
      //   else if (neladejams.chacked == true && ladejams.chacked == false){
      //     console.log("Selected: neladejams");
      //     document.getElementById("ladejams_1").value = "false";
      //   }
        
      //   if (redzamiba.chacked == true) {
      //     console.log("Selected: Redzams");
      //     document.getElementById("redzams_1").value = "true";
      //   } else if (slepts.chacked == true) {
      //     console.log("Selected: Neredzams");
      //     document.getElementById("redzams_1").value = "false";
      //   }
      //   else{
      //     console.log("Selected: none");
          
      //   }
        
      //   break;
     
  }
  if (redzamiba.checked == true && slepts.checked == false) {
      console.log("Selected: Redzams");
      document.getElementById("redzams_1").value = "true";
  } else if (slepts.checked == true && redzamiba.checked == false) {
      console.log("Selected: Neredzams");
      document.getElementById("redzams_1").value = "false";
  }

  if (ladejams.checked == true && neladejams.checked == false) {
      console.log("Selected: Lādējams");
      document.getElementById("ladejams_1").value = "true";
  } else if (neladejams.checked == true && ladejams.checked == false) {
      console.log("Selected: Nelādējams");
      document.getElementById("ladejams_1").value = "false";
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
// Nākotnei
function Notirit() {
  for(let i=0;i<ele.length;i++)
    ele[i].checked = false;
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
function PasaIzvele(redz,lade){
  let redzamiba = document.getElementById("redzams");
  let slepts = document.getElementById("slepts");
  let ladejams = document.getElementById("ladejams");
  let neladejams = document.getElementById("neladejams");
  if(redzamiba.clicked == true)
    rezamiba.checked = true;

}
