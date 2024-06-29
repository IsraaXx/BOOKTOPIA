document.addEventListener('DOMContentLoaded', function() {
    const profileLink = document.getElementById('link');
    const loginForm = document.getElementById('logform');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const buttontype = event.submitter;
            if (buttontype.id === 'btn1') {
                localStorage.setItem('userType', 'Admin');
                window.location.href = "Admin-Profile.html";
            } else if (buttontype.id === 'btn') {
                localStorage.setItem('userType', 'User');
                window.location.href = "User-Profile.html";
            }
        });
    }

    if (profileLink) {
        profileLink.addEventListener('click', function(event) {
            event.preventDefault();
            const userType = localStorage.getItem('userType');

            if (userType === 'Admin') {
                window.location.href='Admin-Profile.html';
            } else if (userType === 'User') {
                window.location.href='User-Profile.html';
            }

         
        });
    }

});
