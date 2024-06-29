    let specialChars = /[&/*#!]/;
document.addEventListener('DOMContentLoaded', function() {
  const signupForm = document.getElementById("signform");
  const username = document.getElementById("username");
  const email = document.getElementById("email");
  const password = document.getElementById("password");
  const passwordconfirm = document.getElementById("password2");

  signupForm.addEventListener("submit", function(e){
    if (!validateInputs()) {
      e.preventDefault();
    }
  });

  function setError(Element , message){
    const inputField = Element.parentElement;
    const displaymessage = inputField.querySelector('.error');

    displaymessage.innerText=message;
    inputField.classList.remove('success');
    inputField.classList.add('error');
    Element.style.borderColor = "#f92c55";
  }

  function setSuccess(Element){
    const inputField = Element.parentElement;
    const displaymessage = inputField.querySelector('.error');

    displaymessage.innerText='';
    inputField.classList.remove('error');
    inputField.classList.add('success');
    Element.style.borderColor = "#61d57e";
  }

  function isValidEmail(email){
    const ch = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return ch.test(String(email).toLowerCase());
  }

  function validateInputs(){
    const usernvalue = username.value.trim();
    const emailvalue = email.value.trim();
    const passwordval = password.value.trim();
    const password2val= passwordconfirm.value.trim();
    let isValid = true;

    if(usernvalue===''){
      setError(username,'Username is required');
      isValid = false;
    } else {
      setSuccess(username);
    }

    if(emailvalue===''){
      setError(email,'Email is required');
      isValid = false;
    } else if(!isValidEmail(emailvalue)){
      setError(email,'Provide a valid email address');
      isValid = false;
    } else {
      setSuccess(email);
    }

    if(passwordval===''){
      setError(password,'Password is required');
      isValid = false;
    } else if(passwordval.length<8){
      setError(password,'Password must be at least 8 characters');
      isValid = false;
    } else if(!(specialChars.test(passwordval))){
      setError(password,'Password should have special characters like /&!#*');
      isValid = false;
    } else {
      setSuccess(password);
    }

    if(password2val==='') {
      setError(passwordconfirm,'Please confirm your password');
      isValid = false;
    } else if (password2val!==passwordval){
      setError(passwordconfirm,"Passwords don't match");
      isValid = false;
    } else {
      setSuccess(passwordconfirm);
    }
    return isValid;
  }
});

