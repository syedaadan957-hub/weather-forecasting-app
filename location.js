const status = document.getElementById("status");
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async function(position){
        const lat = position.coords.latitude.toFixed(5);
        const lon = position.coords.longitude.toFixed(5);
        try{
            const response = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`);
            const data = await response.json();
            const city =
                data.address.city ||
                data.address.town ||
                data.address.village ||
                data.address.county ||
                "Unknown";
            const state = data.address.state || "Unknown";
            const country = data.address.country || "Unknown";
            status.innerHTML = `
            <div class="location-card">

                <div class="location-item">
                    <span>🏙 City</span>
                    <span>${city}</span>
                </div>

                <div class="location-item">
                    <span>🗺 Province</span>
                    <span>${state}</span>
                </div>

                <div class="location-item">
                    <span>🌍 Country</span>
                    <span>${country}</span>
                </div>

                <div class="location-item">
                    <span>📌 Latitude</span>
                    <span>${lat}</span>
                </div>

                <div class="location-item">
                    <span>📍 Longitude</span>
                    <span>${lon}</span>
                </div>

            </div>
            `;
        }
        catch{
            status.innerHTML="Unable to fetch location.";
        }
    });
}
else{
    status.innerHTML="Geolocation not supported.";
}