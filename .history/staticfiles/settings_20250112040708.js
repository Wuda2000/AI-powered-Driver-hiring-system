document.addEventListener('DOMContentLoaded', function() {
    // Language Selection
    const languageSelect = document.getElementById('language-select');
    languageSelect.addEventListener('change', function(event) {
        const selectedLanguage = event.target.value;
        console.log('Language selected:', selectedLanguage);
        // You can implement further logic for language change here
    });

    // Account Icon - Display Profile Picture on Login
    const profilePic = document.getElementById('profile-pic');
    const accountIcon = document.getElementById('account-icon');
    
    // Simulate profile login (you can replace this with actual login status check)
    const loggedIn = true; // Replace with real condition to check login status
    const profileImageUrl = "path/to/profile-picture.jpg"; // Replace with actual profile picture URL
    
    if (loggedIn) {
        accountIcon.style.display = 'none'; // Hide account icon if logged in
        profilePic.src = profileImageUrl;  // Set profile picture source
        profilePic.style.display = 'inline-block'; // Show profile picture
    } else {
        profilePic.style.display = 'none'; // Hide profile picture if not logged in
    }

    // Account Dropdown Menu
    const accountDropdown = document.getElementById('account-dropdown');
    accountIcon.addEventListener('click', function() {
        accountDropdown.style.display = accountDropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Close dropdown if clicked outside
    document.addEventListener('click', function(event) {
        if (!accountIcon.contains(event.target)) {
            accountDropdown.style.display = 'none';
        }
    });
});
