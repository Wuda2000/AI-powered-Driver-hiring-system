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
    $email = $_POST['loginEmail'];
    $password = $_POST['loginPassword'];

    // Validate login credentials
    $sql = "SELECT * FROM users WHERE email = '$email' AND password = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // User found
        header("Location: clients_info.php");  // Redirect to clients page
    } else {
        echo "Invalid credentials or you need to register first.";
    }
}
?>

<form method="post" action="login.php">
    <label for="loginEmail">Email:</label>
    <input type="email" name="loginEmail" required>
    <label for="loginPassword">Password:</label>
    <input type="password" name="loginPassword" required>
    <button type="submit">Login</button>
</form>
