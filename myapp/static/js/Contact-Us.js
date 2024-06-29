document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
  
        var name = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        var message = document.getElementById('message').value;
        var a = 1;
  
      // Validate email format
         var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
         if (!emailRegex.test(email)) {
             alert('Please enter a valid email address.');
             a = 0;
             return;
         }
  
        if (name === '' || email === '' || message === '') {
            alert('Please fill in all required fields!');
            a = 0;
            return;
        }
  
        // Save data to local storage
        if (a == 1) {
            localStorage.setItem('contactName', name);
            localStorage.setItem('contactEmail', email);
            alert('Your message has been sent! Thank you for contacting BOOKTOPIA.');
        }
  
        // Reset the form
        document.getElementById('contactForm').reset();
    });
  });
  