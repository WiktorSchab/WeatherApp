// Generating chart with ChartJS
function createChart(canvasObj, dataG){
    let datas = JSON.parse(dataG)
    const labels = datas.map(entry => entry.time);
    const data = datas.map(entry => entry.temp);
    const descriptions = datas.map(entry => entry.weather_description);

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
                borderColor: '#F6FDFF',
                tension: 0.1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false,
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            let index = context.dataIndex;
                            let temp = context.raw.toFixed(2) + ' °C';
                            let description = descriptions[index];
                            return temp + ' - ' + description;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#FFFFFF',
                        callback: function(value, index, values) {
                            return value + ' °C';
                        }
                    }
                },
                x: {
                    ticks: {
                        color: '#FFFFFF',
                    }
                },
            }

        }
    });

    Chart.defaults.color = '#000';
}

// Function to change displaying chart
function changeChart(num){
    // Getting div that contains all charts
    const divs = document.querySelectorAll('#chartContent div');

    // Loop through each div to find and remove the activeChart ID
    divs.forEach(div => {
        if (div.classList.contains('activeChart')) {
            div.classList.remove('activeChart');
        }
    });

    // Getting chart that will be displayed
    let chartObj = document.getElementById('chartDiv' + num);
    // Adding class that will make chart visible for the user
    chartObj.classList.add('activeChart');
}

// Script to change week day tag on the chart
function changeWeekDayTag(weekDay){
    // Getting object where tag is displayed
    const tag = document.getElementById('weekDay');

    tag.innerHTML = weekDay;
}

// Script to load week day tag on chart when page is loaded
window.onload = function() {
    var firstDayContainer = document.getElementById('firstDayContainer');
    if (firstDayContainer) {
        var firstDayShortName = firstDayContainer.querySelector('p').innerText;
        changeWeekDayTag(firstDayShortName);
    }
};

