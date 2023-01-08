function displaySkillpage(){
    document.getElementById('site-1').style.display='none';
   var b=  document.getElementById('site-2').style.display='block';
   if (b){
    document.body.style.backgroundColor = " rgba(26, 2, 2, 0.804)"

}
else{
    document.body.style.backgroundColor = "white";
}
}

function Cancel(){
    // document.getElementById('site-2').style.display="none";
    document.getElementById('site-1').style.display="block";
    document.body.style.backgroundColor = "white";

}

document.getElementById('skill-area').style.overflow = "visible";