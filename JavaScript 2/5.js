let nombors = [];
let nombor;

while (true) {
    nombor = Number(prompt("Enter a number: "));

    if (nombors.includes(nombor)) {
        console.log("You already entered that number");
        break;
    }

    nombors.push(nombor);
}

nombors.sort((a,b) => a - b);

for (let nombor of nombors) {
    console.log(nombor);
}