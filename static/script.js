let epasts = document.getElementById("epasts");
let epasta_kluda = document.getElementById("epasta_kluda");
let elements = document.getElementById("animacija");
let registret = false;
let ielogot = false;


function EpastaParbaude() {
  if (epasts.value != ""){
    if(!epasts.value.match(/^[A-Za-z\._\-0-9]*@[A-Za-z]*\.[A-Za-z]{2,4}$/)){
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
function VistokluAnimacija(clicked_id) {
  
  if(clicked_id == "varianti1"){
    registret = true;
    elements.classList.add("Vistoklis");
   
  
  }
   if(clicked_id == "varianti2"){
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
  document.getElementById("varianti1").style.visibility = "vissible";
  document.getElementById("varianti2").style.visibility = "vissible";
}
function AnimacijaSakas(){
  SleptPogas();
}
function AnimacijaBeidzas() {
  
  Parslegsanas();
  

  
 
}
//document.addEventListener("load", Sagatavotlapu);

// function Sagatavotlapu() {
//   document.body.classList.remove("fade-out");
//   document.body.classList.remove("fade-in");
//   elements.classList.remove("Vistoklis");
//   elements.classList.remove("Vistoklis2");
//   RaditPogas();
// }
function Parslegsanas() {
  document.body.classList.add("fade-out");

  // If you want to trigger fade-out after a certain time (e.g., 3 seconds), you can use setTimeout
  setTimeout(function () {
    
   
    document.body.classList.add("fade-in");
    if(registret == true){
      window.location.href = "/registresanas";
     
    }
    else if(ielogot == true){
      window.location.href = "/ielogosanas";
      ;
    }
      
  }, 1000); // Adjust the time as needed
 
}