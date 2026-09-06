const status = document.getElementById("status");
const button = document.getElementById("getSuggestions");
button.onclick = function () {
    const crop = document.getElementById("crop").value;
    status.innerHTML = `
        <h3 style="text-align:center;">🤖 AI is analyzing today's weather...</h3>
    `;
    navigator.geolocation.getCurrentPosition(
        async function (position) {
            const response = await fetch("/farming-api/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    crop: crop
                })
            });
            const data = await response.json();
            let html = "";
            data.tips.forEach(function (tip) {
                html += `
                    <div class="tip-card">
                        <h3>${tip.title}</h3>
                        <p>${tip.message}</p>
                    </div>
                `;
            });
            status.innerHTML = html;
        },
        function () {
            status.innerHTML = `
                <h3 style="text-align:center;color:red;">❌ Unable to detect your location.</h3>
            `;
        }
    );
};