<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "James@2542003";
$dbname = "driver_hiring_system";


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'driver_hiring',  # Change this to your DB name
        'USER': 'root',  # Your DB user
        'PASSWORD': 'James@2542003',  # Your DB password
        'HOST': 'localhost',  # Use localhost for local development
        'PORT': '3306',  # Default MySQL port
    }




// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get user credentials
$email = $_POST['email'];
$password = $_POST['password'];

// Check credentials in the database
$sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Login successful!";
} else {
    echo "Invalid credentials!";
}

$conn->close();
?>


<form method="post" action="login.php">
    <label for="loginEmail">Email:</label>
    <input type="email" name="loginEmail" required>
    <label for="loginPassword">Password:</label>
    <input type="password" name="loginPassword" required>
    <button type="submit">Login</button>
</form>
