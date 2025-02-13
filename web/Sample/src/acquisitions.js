import Chart from 'chart.js/auto'

  const data = {
    labels: [
      'Strength', 'Endurance', 'Flexibility', 'Speed', 'Agility', 'Balance', 'Coordination'
    ],
    datasets: [{
      label: 'Athlete A',
      data: [80, 70, 60, 90, 85, 75, 80],
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    }, {
      label: 'Athlete B',
      data: [60, 85, 75, 80, 70, 90, 65],
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgb(54, 162, 235)',
      pointBackgroundColor: 'rgb(54, 162, 235)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(54, 162, 235)'
    }]
  };

  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'radar',
      data: data,
      options: {
        elements: {
          line: {
            borderWidth: 3
          }
        }
      },
    }
  );

