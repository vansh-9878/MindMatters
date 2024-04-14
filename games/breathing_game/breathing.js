

document.getElementById('startButton').addEventListener('click', () => {
    const circle = document.getElementById('circle');
    circle.style.transform = 'scale(1.2)';
    setTimeout(() => {
      circle.style.transform = 'scale(1)';
    }, 4000);
  
    // Repeat the breathing exercise every 8 seconds until 1 minute has passed
    const interval = setInterval(() => {
      circle.style.transform = 'scale(1.2)';
      setTimeout(() => {
        circle.style.transform = 'scale(1)';
      }, 4000);
    }, 8000);
  
    // Stop the breathing exercise after 1 minute
    setTimeout(() => {
      clearInterval(interval);
    }, 60000);
  });