let nums = [];
let value;

while (true) {
    value = Number(prompt("Enter a number (0 to stop): "));
    if (value === 0) {
        break;
}

nums.push(value);
}

nums.sort((a, b) => b - a)

for (let n of nums) {
    console.log(n);
}
