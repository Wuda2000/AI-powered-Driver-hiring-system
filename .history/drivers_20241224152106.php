<?php
// Database connection settings
$servername = "localhost"; // Host
$username = "root"; // MySQL username
$password = "James@254"; // MySQL password (empty if you have no password)
$dbname = "driver_hiring"; // Database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname, 3306); // Ensure using port 3306

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to fetch driver data
$sql = "SELECT id, name, experience FROM drivers";
$result = $conn->query($sql);

// Check if the query returns results
if ($result->num_rows > 0) {
    // Initialize an array to hold the driver data
    $drivers = [];

    // Fetch each row as an associative array
    while($row = $result->fetch_assoc()) {
        $drivers[] = [
            "id" => $row["id"],
            "name" => $row["name"],
            "experience" => $row["experience"]
        ];
    }

    // Output the driver data as JSON
    echo json_encode($drivers);
} else {
    echo json_encode([]);
}

// Close the database connection
$conn->close();
?>
