const weatherDiv = document.getElementById("weather");
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position){
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        fetch("/weather/",{
            method:"POST",
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken":getCookie("csrftoken")
            },
            body:JSON.stringify({
                latitude:lat,
                longitude:lon
            })
        })
        .then(response=>response.json())
        .then(weather=>{
            const current = weather.current;
            const rawDate = current.time.split("T")[0];
            const date = new Date(rawDate).toLocaleDateString("en-GB",{
                day:"numeric",
                month:"long",
                year:"numeric"
            });
            const time = current.time.split("T")[1];
            weatherDiv.innerHTML = `
            <div class="weather-card">

                <div class="weather-item">
                    <span>🌡 Temperature</span>
                    <span>${current.temperature_2m} °C</span>
                </div>

                <div class="weather-item">
                    <span>💧 Humidity</span>
                    <span>${current.relative_humidity_2m}%</span>
                </div>

                <div class="weather-item">
                    <span>💨 Wind Speed</span>
                    <span>${current.wind_speed_10m} km/h</span>
                </div>

                <div class="weather-item">
                    <span>🌧 Rain Probability</span>
                    <span>${weather.daily.precipitation_probability_max[0]}%</span>
                </div>

                <div class="weather-item">
                    <span>📅 Date</span>
                    <span>${date}</span>
                </div>

                <div class="weather-item">
                    <span>🕒 Time</span>
                    <span>${time}</span>
                </div>

            </div>
            `;
        });
    });
}