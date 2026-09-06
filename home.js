const alertText = document.getElementById("alertText");
const alertDot = document.getElementById("alertDot");
const popupOverlay = document.getElementById("popupOverlay");
const popupContent = document.getElementById("popupContent");
const popupBtn = document.getElementById("popupBtn");
navigator.geolocation.getCurrentPosition(async function(position){
    const response = await fetch("/alerts-api/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            latitude:position.coords.latitude,
            longitude:position.coords.longitude
        })
    });
    const data = await response.json();
    if(data.count===0){
        alertText.innerHTML="🟢 No Active Alerts";
        alertDot.style.display="none";
        return;
    }
    alertText.innerHTML=`🔴 ${data.count} Active Alert(s)`;
    alertDot.style.display="inline-block";
    let html = `
    <h3>🔴 ${data.count} Active Alert(s)</h3>
    <p>Your farm may experience the following weather conditions:</p>
    <ul>
    `;
    data.alerts.forEach(alert=>{
        html += `<li>${alert.icon} ${alert.title}</li>`;
    });
    html += `
    </ul>
    <p style="margin-top:15px;">
    Review the detailed recommendations before planning today's farming activities.
    </p>
    `;
    popupContent.innerHTML = html;
    popupOverlay.style.display="flex";
});
popupBtn.onclick=function(){
    popupOverlay.style.display="none";

};
document.getElementById("viewAlerts").onclick=function(){
    window.location.href="/alerts/";
};