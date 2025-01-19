<?php
// Connect to the database
$servername = "localhost";
$username = "root"; // Use your database username
$password = ""; // Use your database password
$dbname = "driver_hiring";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query the database
$sql = "SELECT name, experience FROM drivers";
$result = $conn->query($sql);

// Fetch data as an array
$drivers = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $drivers[] = $row;
    }
}

// Output data as JSON
header('Content-Type: application/json');
echo json_encode($drivers);

// Close the connection
$conn->close();
?>
