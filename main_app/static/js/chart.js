document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('lineChart');
    if (!canvas) return;
  
    try {
      const labels = JSON.parse(canvas.dataset.labels);
      const expenses = JSON.parse(canvas.dataset.expenses);
      const salaries = JSON.parse(canvas.dataset.salaries);
  
      console.log("Labels:", labels);
      console.log("Expenses:", expenses);
      console.log("Salaries:", salaries);
  
      new Chart(canvas, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Expenses ($)',
              data: expenses,
              borderColor: 'rgba(220, 53, 69, 0.9)',
              backgroundColor: 'rgba(220, 53, 69, 0.1)',
              tension: 0.3,
              fill: true,
            },
            {
              label: 'Salary ($)',
              data: salaries,
              borderColor: 'rgba(25, 135, 84, 0.9)',
              backgroundColor: 'rgba(25, 135, 84, 0.1)',
              tension: 0.3,
              fill: true,
            }
          ]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 100 // 👈 Y-axis increments by 100
              },
              title: {
                display: true,
                text: 'Amount ($)',
                font: {
                  size: 14
                }
              }
            }
          }
        }
      });
    } catch (error) {
      console.error('Chart.js error:', error);
    }
  });
  