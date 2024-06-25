// Użycie danych w JavaScript
function createChart(canvasObj, dataG){


    let datas = JSON.parse(dataG)
    const labels = datas.map(entry => entry.time);
    const data = datas.map(entry => entry.temp);

    // Debug
    //console.log(canvasObj);
    //console.log(datas);

    var ctx = document.getElementById(canvasObj).getContext('2d');
    var temperatureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Temperature',
                data: data,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
