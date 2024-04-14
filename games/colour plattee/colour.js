const colors = ['#FF5733', '#FFC300', '#FF5733', '#FFC300', '#FF5733', '#FFC300']; // Array of colors for the palette
let correctColorIndex; // Index of the correct color in the palette

const colorPalette = document.getElementById('colorPalette');
const startButton = document.getElementById('startButton');
const pass=document.querySelector(".pass");
const fail=document.querySelector(".fail");


// Function to shuffle array randomly
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Function to create color palette
function createPalette() {
  shuffleArray(colors);
  colorPalette.innerHTML = '';
  colors.forEach((color, index) => {
    const colorBox = document.createElement('div');
    colorBox.classList.add('color-box');
    colorBox.style.backgroundColor = color;
    colorBox.addEventListener('click', () => checkColor(index));
    colorPalette.appendChild(colorBox);
  });
}

// Function to start the game
function startGame() {
    pass.classList.add("pass");
    fail.classList.add("fail");
  createPalette();
  correctColorIndex = Math.floor(Math.random() * colors.length);
}

// Function to check selected color
function checkColor(index) {
  if (index === correctColorIndex) {
    // alert('Correct! You matched the color.');
    pass.classList.remove("pass");
    
    startGame(); // Start a new game after correct match
  } else {
    // alert('Incorrect! Try again.');
    fail.classList.remove("fail");
    setTimeout(() => {
        fail.classList.toggle("fail");
      }, 1000);
  }
}

// Event listener for start button
startButton.addEventListener('click', startGame);

// Initialize game
startGame();
