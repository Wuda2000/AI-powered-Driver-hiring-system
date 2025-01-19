<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "driver_hiring_system";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['registerName'];
    $email = $_POST['registerEmail'];
    $password = $_POST['registerPassword'];

    // Check if user already exists
    $sql = "SELECT * FROM users WHERE email = '$email'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        echo "User already exists!";
    } else {
        // Register user
        $sql = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$password')";
        if ($conn->query($sql) === TRUE) {
            echo "Registration successful!";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
}
?>

<form method="post" action="register.php">
    <label for="registerName">Name:</label>
    <input type="text" name="registerName" required>
    <label for="registerEmail">Email:</label>
    <input type="email" name="registerEmail" required>
    <label for="registerPassword">Password:</label>
    <input type="password" name="registerPassword" required>
    <button type="submit">Register</button>
</form>
