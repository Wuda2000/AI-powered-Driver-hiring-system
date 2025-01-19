document.getElementById('fetchDriversBtn').addEventListener('click', () => {
    fetch('/api/drivers')
        .then(response => response.json())
        .then(data => {
            const driverList = document.getElementById('driverList');
            driverList.innerHTML = '';

            data.forEach(driver => {
                const driverItem = document.createElement('div');
                driverItem.innerText = `${driver.name} - ${driver.experience} years of experience`;
                driverList.appendChild(driverItem);
            });
        })
        .catch(err => console.error('Error fetching drivers:', err));
});
