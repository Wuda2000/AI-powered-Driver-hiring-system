<?php
// Sample PHP script to return driver data
header('Content-Type: application/json');

$drivers = [
    ["name" => "John Doe", "experience" => 5],
    ["name" => "Jane Smith", "experience" => 3],
    ["name" => "James Brown", "experience" => 8],
];

echo json_encode($drivers);
?>
