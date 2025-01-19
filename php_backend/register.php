<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "James@2542003";
$dbname = "driver_hiring_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get user data from the form
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['registerName'];
    $email = $_POST['registerEmail'];
    $password = $_POST['registerPassword'];

    // Hash the password before storing it
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert data into the database
    $sql = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$hashed_password')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>

<!-- Registration Form -->
<form method="post" action="register.php">
    <label for="registerName">Name:</label>
    <input type="text" name="registerName" required>
    <label for="registerEmail">Email:</label>
    <input type="email" name="registerEmail" required>
    <label for="registerPassword">Password:</label>
    <input type="password" name="registerPassword" required>
    <button type="submit">Register</button>
</form>
