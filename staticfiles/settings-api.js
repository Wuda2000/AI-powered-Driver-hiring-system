function updateSettings(data) {
    fetch('/api/settings/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Settings updated:', data);
    })
    .catch(error => {
        console.error('Error updating settings:', error);
    });
}
