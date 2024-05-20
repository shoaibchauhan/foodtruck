document.addEventListener("DOMContentLoaded", function() {
    const map = L.map('map').setView([37.7749, -122.4194], 13); // Default to San Francisco

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    async function findFoodTrucks() {
        const latitude = document.getElementById("latitude").value;
        const longitude = document.getElementById("longitude").value;

        if (!latitude || !longitude) {
            alert("Please enter both latitude and longitude");
            return;
        }

        try {
            const response = await fetch(`/api/food?latitude=${latitude}&longitude=${longitude}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`An error occurred: ${response.statusText}`);
            }

            const foodTrucks = await response.json();
            console.log('Received food trucks:', foodTrucks); // Debugging line
            map.setView([latitude, longitude], 15);

            // Clear existing markers
            map.eachLayer(layer => {
                if (layer instanceof L.Marker) {
                    map.removeLayer(layer);
                }
            });

            foodTrucks.forEach(truck => {
                console.log('Adding marker for truck:', truck); // Debugging line
                L.marker([truck.Latitude, truck.Longitude])
                  .addTo(map)
                  .bindPopup(`<b>${truck.Applicant}</b><br>${truck.Address}<br>${truck.FoodItems}`)
                  .openPopup();
            });
        } catch (error) {
            console.error('Error fetching food trucks:', error);
            alert('An error occurred while fetching food trucks. Please try again later.');
        }
    }

    window.findFoodTrucks = findFoodTrucks;
});
