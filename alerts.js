const alertsDiv = document.getElementById("alerts");
navigator.geolocation.getCurrentPosition(function(position){
    fetch("/alerts-api/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify({
            latitude:position.coords.latitude,
            longitude:position.coords.longitude
        })
    })
    .then(response => response.json())
    .then(data => {
        // No active alerts
        if(data.count === 0){
            alertsDiv.innerHTML = `
                <div class="no-alert-card">
                    <h2>✅ No Active Alerts</h2>
                    <p>No severe weather conditions are expected for today or tomorrow.</p>
                    <p>Your farm is currently safe.</p>
                </div>
            `;
            return;
        }
        // Display only active alerts
        let html = "";
        data.alerts.forEach(alert => {
            let recommendations = "";
            alert.recommendation.forEach(item => {
                recommendations += `<li>${item}</li>`;
            });
            html += `
            <div class="alert-card">
                <h2>${alert.icon} ${alert.title}</h2>
                <p><strong>Date:</strong> ${alert.date}</p>
                <p><strong>Severity:</strong> ${alert.severity}</p>
                <p>${alert.message}</p>
                <h3>Recommendations</h3>
                <ul>${recommendations}</ul>
            </div>
            `;
        });
        alertsDiv.innerHTML = html;
    });
},
function(){
    alertsDiv.innerHTML = `
        <div class="no-alert-card">
            <h2>❌ Location Required</h2>
            <p>Please allow location access to receive AI weather alerts.</p>
        </div>
    `;
});