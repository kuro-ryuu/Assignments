document.getElementById("task5.1").innerHTML = "<h3>Task 5 result: </h3>";

const year = parseInt(prompt("Enter the year"))
function checkLeap() {
    if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0) {
        return true;
    } else {
        return false;
    }
}



document.getElementById("task5.2").innerText = checkLeap();