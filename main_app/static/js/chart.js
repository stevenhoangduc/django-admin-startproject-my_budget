document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('expenseChart');
    if (!canvas) return;
  
    try {
      const labels = JSON.parse(document.getElementById('labels-data').textContent);
      const values = JSON.parse(document.getElementById('values-data').textContent);
  
      console.log("Raw labels:", labels);
      console.log("Raw values:", values);
  
      new Chart(canvas, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Monthly Expenses ($)',
            data: values,
            backgroundColor: 'rgba(203, 32, 52, 0.7)',
            borderRadius: 6,
            borderSkipped: false
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: function(context) {
                  return `$${context.parsed.y.toFixed(2)}`;
                }
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    } catch (error) {
      console.error('Chart.js error:', error);
    }
  });
  