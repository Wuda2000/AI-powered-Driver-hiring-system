<?php
// Database connection
$servername = "localhost";
$username = "your_mysql_user";
$password = "your_mysql_password";
$dbname = "driver_hiring_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get user data
$name = $_POST['name'];
$email = $_POST['email'];
$password = $_POST['password']; // Note: Never store passwords as plain text in a real app

// Insert data into the database
$sql = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$password')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
