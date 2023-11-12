function extractAvgDailyHours(data) {
    return data.map(item => {
        const fields = Object.keys(item)[0].split(';');
        const values = Object.values(item)[0].split(';');
        const index = fields.indexOf('AvgDailyHours');
        return parseFloat(values[index]);
    });
}

function extractLeavesTaken(data) {
    return data.map(item => {
        const fields = Object.keys(item)[0].split(';');
        const values = Object.values(item)[0].split(';');
        const index = fields.indexOf('LeavesTaken');
        return parseFloat(values[index]);
    });
}
function updateChart(chartId, label, data, backgroundColor, borderColor) {
    var ctx = document.getElementById(chartId).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map((_, index) => `Employee ${index + 1}`),
            datasets: [{
                label: label,
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
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

// When you get the id just update the value
const id = 200001;

function fetchAndDisplayData() {
    fetch(`http://127.0.0.1:5000/employees?id=${id}`)  // Adjust the URL as needed
        .then(response => response.json())
        .then(data => {
            const avgDailyHours = data[0].AvgDailyHours
            const leavesTaken = data[0].LeavesTaken;

            updateChart('avgDailyHoursChart', 'Average Daily Hours', avgDailyHours, 'rgba(75, 192, 192, 0.2)', 'rgba(75, 192, 192, 1)');
            updateChart('leavesTakenChart', 'Leaves Taken', leavesTaken, 'rgba(255, 159, 64, 0.2)', 'rgba(255, 159, 64, 1)');
        })
        .catch(error => console.error('Error:', error));
}
