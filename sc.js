function login(answer)
{
//  for(;;)
//  {
//      let answer = +prompt("Ответ на главный вопорос о Вселенной и всём таком");
      if(answer != 42) {
          alert ("Это не так");
        }
      else {
          $(".login").hide();
      }
//  }
}

function camon()
{
  
   if(document.getElementById("Camera").style.visibility == "visible")
   {
     document.getElementById("Camera").style.visibility = "collapse";
     document.getElementById("btcam").innerHTML="Посматреть в камеру";
   }
   else
   {
     document.getElementById("btcam").innerHTML="Выключить просмотр";
     document.getElementById("Camera").style.visibility = "visible";
   }
}