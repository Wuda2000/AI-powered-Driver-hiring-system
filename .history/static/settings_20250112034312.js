document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    // Perform form validation and then update settings
    if(name && email) {
        console.log('Profile updated:', { name, email });
        // You can call an API to save this data in your backend
    } else {
        alert('Please fill out all fields');
    }
});

document.getElementById('email-notifications').addEventListener('change', function(event) {
    const notificationsEnabled = event.target.checked;
    console.log('Email notifications:', notificationsEnabled);
    // You can call an API to update this setting in your backend
});

document.getElementById('profile-visibility').addEventListener('change', function(event) {
    const visibilityEnabled = event.target.checked;
    console.log('Profile visibility:', visibilityEnabled);
    // Call an API to update this setting in your backend
});
