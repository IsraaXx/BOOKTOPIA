function toggleVisibility() {
    var div = document.getElementById("restparagraph");
    var  btnreadmore = document.querySelector(" .btnreadmore");

    if (div.style.display === "none") {
      div.style.display = "block";
      btnreadmore.textContent = "Read Less";
    } else {
      div.style.display = "none";
      btnreadmore.textContent = "Read More";
    }
  }
  function Borrow(){
    var c = document.getElementById("AlertMessage");
    c.style.opacity = '1';
    c.style.transition = 'opacity 0.5s ease';
    setTimeout(hideMessage,5000);
 }
 function hideMessage() {
  var c = document.getElementById("AlertMessage");
  c.style.opacity = '0';
}
