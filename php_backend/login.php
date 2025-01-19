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

// Get user credentials from the form
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['loginEmail'];
    $password = $_POST['loginPassword'];

    // Use prepared statement to prevent SQL injection
    $stmt = $conn->prepare("SELECT id, name, password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    // Check if email exists
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($id, $name, $hashed_password);
        $stmt->fetch();

        // Verify the password
        if (password_verify($password, $hashed_password)) {
            echo "Login successful!";
        } else {
            echo "Invalid credentials!";
        }
    } else {
        echo "Invalid credentials!";
    }

    $stmt->close();
}

$conn->close();
?>

<!-- Login Form -->
<form method="post" action="login.php">
    <label for="loginEmail">Email:</label>
    <input type="email" name="loginEmail" required>
    <label for="loginPassword">Password:</label>
    <input type="password" name="loginPassword" required>
    <button type="submit">Login</button>
</form>
