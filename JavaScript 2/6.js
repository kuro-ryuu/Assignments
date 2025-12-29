roll_results = [];
roll_a_six = 0;


function dice() {
    return Math.floor(Math.random() * 6) + 1;
}


while (roll_a_six != 6) {
    roll_a_six = dice();
    roll_results.push(roll_a_six);
}

const ul = document.getElementById("rolls");

for (let roll of roll_results) {
    const li = document.createElement("li");
    li.textContent = roll;
    ul.appendChild(li);
}