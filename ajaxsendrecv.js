function getXmlHttp(){
    var xmlhttp;
    try {
      xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
      try {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
      } catch (E) {
        xmlhttp = false;
      }
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
      xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
  }
  
function doLoad(value) {
//     // Create new JsHttpRequest object.
//     var req = new XMLHttpRequest();
//     // Code automatically called on load finishing.
//     req.onreadystatechange = function() {
//         if (req.readyState == 4)
//         {
//             $("#temppi").value =  req.responseText;

//         }
//     }
//         // Prepare request object (automatically choose GET or POST).
// //        req.open(null, 'http://172.16.1.45/cgi-bin/t.py', true);
//         req.open('GET', 'robots.txt', true);
//         req.send();


var req = getXmlHttp()

req.open('GET', 'temppi.php', true);
req.onreadystatechange = function() {
  if (req.readyState == 4) {
     if(req.status == 200) {
       $("#temppi").html(  req.responseText);
       //alert(req.responseText);
	 }
  }
};
req.send(null); 

}


var timeout = 1;
var timeout2 = 1;


function doLoadNext()
{
  doLoad(true);
  clearTimeout(timeout);
  timeout = setTimeout("doLoadNext1()", 3000);

}
function doLoadNext1()
{
//  doLoad(document.getElementById('FSV'));
  doLoad(true);
  clearTimeout(timeout2);
  timeout2 = setTimeout("doLoadNext()", 3000);
}
//  if (timeout) clearTimeout(timeout);
  timeout = setTimeout("doLoadNext()", 100);
//  timeout2 = setTimeout("doLoad(true)", 3000);
