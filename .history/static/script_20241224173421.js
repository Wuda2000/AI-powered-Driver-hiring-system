// Fetch drivers from the API
fetch('/drivers/')
    .then(response => response.json())
    .then(data => {
        const driverList = document.getElementById('driver-list');
        
        // Loop through the driver data and create list items
        data.forEach(driver => {
            const listItem = document.createElement('li');
            listItem.textContent = `${driver.name} - ${driver.experience} years of experience`;
            driverList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Error fetching driver data:', error);
    });
