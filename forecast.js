function getWeatherInfo(code){
    if(code == 0){
        return {
            icon:"☀️",
            text:"Clear Sky"
        };
    }
    else if([1,2,3].includes(code)){
        return {
            icon:"⛅",
            text:"Partly Cloudy"
        };
    }
    else if([45,48].includes(code)){
        return {
            icon:"🌫️",
            text:"Fog"
        };
    }
    else if([51,53,55].includes(code)){
        return {
            icon:"🌦️",
            text:"Drizzle"
        };
    }
    else if([61,63,65,80,81,82].includes(code)){
        return {
            icon:"🌧️",
            text:"Rain"
        };
    }
    else if([71,73,75].includes(code)){
        return {
            icon:"❄️",
            text:"Snow"
        };
    }
    else if(code == 95){
        return {
            icon:"⛈️",
            text:"Thunderstorm"
        };
    }
    return {
        icon:"🌤️",
        text:"Weather"
    };
}
const forecastDiv = document.getElementById("forecast");
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
            const daily = weather.daily;
            let html = "";
            for(let i=0;i<10;i++){
                const date = new Date(daily.time[i]);
                const day = date.toLocaleDateString("en-US",{
                    weekday:"long"
                });
                const fullDate = date.toLocaleDateString("en-GB",{
                    day:"numeric",
                    month:"short"
                });
                const maxTemp = daily.temperature_2m_max[i];
                const minTemp = daily.temperature_2m_min[i];
                const rain = daily.precipitation_probability_max[i];
                const weatherCode = daily.weather_code[i];
                const weather = getWeatherInfo(weatherCode);
                html += `
                <div class="forecast-card">
                    <h2>${weather.icon} ${day}</h2>
                    <p><b>${weather.text}</b></p>
                    <p>📅 ${fullDate}</p>
                    <div class="forecast-item">
                        <span>🌡 Maximum</span>
                        <span>${maxTemp}°C</span>
                    </div>
                    <div class="forecast-item">
                        <span>❄ Minimum</span>
                        <span>${minTemp}°C</span>
                    </div>
                    <div class="forecast-item">
                        <span>🌧 Rain Chance</span>
                        <span>${rain}%</span>
                    </div>
                </div>
                `;
            }
            forecastDiv.innerHTML = html;
        });
    });
}