// Fetch drivers from the API
fetch('/api/drivers/')  // Make sure this matches the pattern in website/urls.py

    .then(response => response.json())
    .then(data => {
        const driverList = document.getElementById('driver-list');
        
        // Loop through the driver data and create list items
        data.forEach(driver => {
            const listItem = document.createElement('li');
            
            // Create the image element if image_url is defined
            const driverImage = document.createElement('img');
            const imageUrl = driver.image_url ? `/static/images/${driver.image_url}` : '/static/images/default-driver.jpg';  // Default image if no URL is provided
            driverImage.src = imageUrl;
            driverImage.alt = `${driver.name}'s Image`;  // Set alt text for the image

            // Add the image and text content to the list item
            listItem.appendChild(driverImage);
            listItem.innerHTML += `${driver.name} - ${driver.experience} years of experience`;
            
            // Append the list item to the driver list
            driverList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Error fetching driver data:', error);
    });
