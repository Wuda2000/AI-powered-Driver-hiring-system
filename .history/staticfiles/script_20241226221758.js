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
  
          // Build the driver card HTML with fixed star rating logic
          
        });
      })
      .catch(error => console.error('Error fetching driver data:', error));
  };