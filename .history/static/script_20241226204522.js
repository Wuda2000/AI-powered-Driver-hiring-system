window.onload = function() {
    fetch('/api/drivers/')
        .then(response => {
            // If the response is not ok, throw an error
            if (!response.ok) {
                throw new Error('Error fetching driver data');
            }
            return response.json();
        })
        .then(data => {
            const driverList = document.getElementById('driver-list');
            data.forEach(driver => {
                const driverCard = `
                    <div class="col-md-4 driver-card">
                        <img src="/static/images/${driver.image_url}" class="rounded-circle" alt="${driver.name}" width="80" height="100">
                        <h3>${driver.name}</h3>
                        <p>Experienced driver ready to serve</p>
                        <div class="experience">${driver.experience} years of experience</div>
                       <ul>
    ${'★'.repeat(Number(driver.experience) || 0)}${'☆'.repeat(5 - (Number(driver.experience) || 0))}
</ul>

                        <button class="buy-btn">Hire Now</button>
                    </div>
                `;
                driverList.innerHTML += driverCard;
            });
        })
        .catch(error => console.error('Error fetching driver data:', error));
};
