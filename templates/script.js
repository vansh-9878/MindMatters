//GAME 1

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
    




//GAME 2

    val_c1 = 1
        val_c2 = 1
        val_c3 = 1
        val_c4 = 1
        val_c5 = 1
        val_c6 = 1
        val_c7 = 1
        turn = 1


        //checking the winner

        function check(player) {
            setTimeout(() => {

                for (i = 1; i <= 7; i++) {
                    for (j = 1; j <= 3; j++) {
                        if (document.getElementById(`c${i}r${j}`).style.backgroundColor == `${player}` && document.getElementById(`c${i}r${j + 1}`).style.backgroundColor == `${player}` && document.getElementById(`c${i}r${j + 2}`).style.backgroundColor == `${player}` && document.getElementById(`c${i}r${j + 3}`).style.backgroundColor == `${player}`) {
                            alert(`${player} wins`)
                            location.reload()
                        }

                    }
                }

                for (i = 1; i <= 6; i++) {
                    for (j = 1; j <= 4; j++) {
                        if (document.getElementById(`c${j}r${i}`).style.backgroundColor == `${player}` && document.getElementById(`c${j + 1}r${i}`).style.backgroundColor == `${player}` && document.getElementById(`c${j + 2}r${i}`).style.backgroundColor == `${player}` && document.getElementById(`c${j + 3}r${i}`).style.backgroundColor == `${player}`) {
                            alert(`${player} wins`)
                            location.reload()
                        }

                    }

                }

                for (i = 1; i <= 4; i++) {
                    for (j = 1; j <= 3; j++) {
                        if (document.getElementById(`c${i}r${j}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 1}r${j + 1}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 2}r${j + 2}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 3}r${j + 3}`).style.backgroundColor == `${player}`) {
                            alert(`${player} wins`)
                            location.reload()
                        }

                    }
                }

                for (i = 1; i <= 4; i++) {
                    for (j = 6; j >= 4; j--) {
                        if (document.getElementById(`c${i}r${j}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 1}r${j - 1}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 2}r${j - 2}`).style.backgroundColor == `${player}` && document.getElementById(`c${i + 3}r${j - 3}`).style.backgroundColor == `${player}`) {
                            alert(`${player} wins`)
                            location.reload()
                        }

                    }
                }

            }, 200)

        }



        //playing
        document.querySelectorAll(".column").forEach((e) => {
            e.addEventListener("click", () => {

                sum = eval(`val_${e.id}`)
                eval(`val_${e.id}++`)


                if (sum <= 6 && turn % 2 != 0) {
                    document.getElementById(`${e.id}r${sum}`).style.backgroundColor = "red"
                    turn++
                    check('red')
                    document.getElementById("whosturn").innerText = "Yellow's Turn"
                }
                
                else if (sum <= 6 && turn % 2 == 0) {
                    document.getElementById(`${e.id}r${sum}`).style.backgroundColor = "yellow"
                    turn++
                    check('yellow')
                    document.getElementById("whosturn").innerText = "Red's Turn"

                }
            })
        })




//GAME 3

let words = [
    {
        word: "addition",
        hint: "The process of adding numbers"
    },
    {
        word: "meeting",
        hint: "Event in which people come together"
    },
    {
        word: "number",
        hint: "Math symbol used for counting"
    },
    {
        word: "exchange",
        hint: "The act of trading"
    },
    {
        word: "canvas",
        hint: "Piece of fabric for oil painting"
    },
    {
        word: "garden",
        hint: "Space for planting flower and plant"
    },
    {
        word: "position",
        hint: "Location of someone or something"
    },
    {
        word: "feather",
        hint: "Hair like outer covering of bird"
    },
    {
        word: "comfort",
        hint: "A pleasant feeling of relaxation"
    },
    {
        word: "tongue",
        hint: "The muscular organ of mouth"
    },
    {
        word: "expansion",
        hint: "The process of increase or grow"
    },
    {
        word: "country",
        hint: "A politically identified region"
    },
    {
        word: "group",
        hint: "A number of objects or persons"
    },
    {
        word: "taste",
        hint: "Ability of tongue to detect flavour"
    },
    {
        word: "store",
        hint: "Large shop where goods are traded"
    },
    {
        word: "field",
        hint: "Area of land for farming activities"
    },
    {
        word: "friend",
        hint: "Person other than a family member"
    },
    {
        word: "pocket",
        hint: "A bag for carrying small items"
    },
    {
        word: "needle",
        hint: "A thin and sharp metal pin"
    },
    {
        word: "expert",
        hint: "Person with extensive knowledge"
    },
    {
        word: "statement",
        hint: "A declaration of something"
    },
    {
        word: "second",
        hint: "One-sixtieth of a minute"
    },
    {
        word: "library",
        hint: "Place containing collection of books"
    },
]
      const wordText = document.querySelector(".word"),
      hintText = document.querySelector(".hint span"),
      timeText = document.querySelector(".time b"),
      inputField = document.querySelector("input"),
      refreshBtn = document.querySelector(".refresh-word"),
      checkBtn = document.querySelector(".check-word");
      game3=document.querySelector(".game3");
      btn3=document.querySelector(".fix");

      let correctWord, timer;

      const initTimer = maxTime => {
          clearInterval(timer);
          timer = setInterval(() => {
              if(maxTime > 0) {
                  maxTime--;
                  return timeText.innerText = maxTime;
              }
              alert(`Time off! ${correctWord.toUpperCase()} was the correct word`);
              initGame();
          }, 1000);
      }

      const initGame = () => {
        
          initTimer(30);
          let randomObj = words[Math.floor(Math.random() * words.length)];
          let wordArray = randomObj.word.split("");
          for (let i = wordArray.length - 1; i > 0; i--) {
              let j = Math.floor(Math.random() * (i + 1));
              [wordArray[i], wordArray[j]] = [wordArray[j], wordArray[i]];
          }
          wordText.innerText = wordArray.join("");
          hintText.innerText = randomObj.hint;
          correctWord = randomObj.word.toLowerCase();;
          inputField.value = "";
          inputField.setAttribute("maxlength", correctWord.length);
      }


        btn3.addEventListener("click",()=>{
            initGame();
        })


    //   if(game3.classList.contains(".escape")){
    //     console.log("heyy");
    //   }else{
    //     
    //   }
      

      const checkWord = () => {
          let userWord = inputField.value.toLowerCase();
          if(!userWord) return alert("Please enter the word to check!");
          if(userWord !== correctWord) return alert(`Oops! ${userWord} is not a correct word`);
          alert(`Congrats! ${correctWord.toUpperCase()} is the correct word`);
          initGame();
      }

      refreshBtn.addEventListener("click", initGame);
      checkBtn.addEventListener("click", checkWord);




//DISPLAY with BUTTON

btn1=document.querySelector(".col");
btn2=document.querySelector(".con");

game1=document.querySelector(".game1");
game2=document.querySelector(".game2");

shut1=document.querySelector(".set1");
shut2=document.querySelector(".set2");
shut3=document.querySelector(".set3");


function disapper(){
    game1.classList.add("escape");
    game2.classList.add("escape");
    game3.classList.add("escape");
}


btn1.addEventListener("click",function(){
    disapper();
    game1.classList.remove("escape");
})

btn2.addEventListener("click",function(){
    disapper();
    game2.classList.remove("escape");
})

btn3.addEventListener("click",function(){
    disapper();
    game3.classList.remove("escape");
})

shut1.addEventListener("click",function(){
    disapper();
})

shut2.addEventListener("click",function(){
    disapper();
})
shut3.addEventListener("click",function(){
    disapper();
})



