window.onload = function() { 
    fetch('/api/drivers/')
    .then(response => {
        // Check if the response is okay (status 200)
        if (!response.ok) {
            throw new Error('Error fetching driver data');
        }
        // Log the response to inspect its structure
        return response.json();
    })
    .then(data => {
        console.log(data); // Add this line to log the response
        const driverList = document.getElementById('driver-list');
        data.forEach(driver => {
            console.log(driver.name, driver.experience); // Log each driver's name and experience
            let experience = Number(driver.experience) || 0;
            console.log(experience); // Ensure experience is being correctly parsed
            
            // Build the driver card HTML
            const driverCard = `
                <div class="col-md-4 driver-card">
                    <img src="/static/images/${driver.image_url}" class="rounded-circle" alt="${driver.name}" width="80" height="100">
                    <h3>${driver.name}</h3>
                    <p>Experienced driver ready to serve</p>
                    <div class="experience">${experience} years of experience</div>
                    <ul>
                        ${'★'.repeat(experience)}${'☆'.repeat(5 - experience)}  <!-- Handle star rendering -->
                    </ul>
                    <button class="buy-btn">Hire Now</button>
                </div>
            `;
            driverList.innerHTML += driverCard;
        });
    })
    .catch(error => console.error('Error fetching driver data:', error));
};
