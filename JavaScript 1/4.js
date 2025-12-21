const room_picking = Math.floor(Math.random() * 4) + 1;

console.log("The random number is: " + room_picking);

document.getElementById("task4.1").innerHTML = "<h3>Task 4 result: </h3>";

if (room_picking == 1) {
    document.getElementById("task4.2").innerText = "Gryffindor"
}
else if (room_picking == 2) {
    document.getElementById("task4.2").innerText = "Slytherin"
}
else if (room_picking == 3) {
    document.getElementById("task4.2").innerText = "Hufflepuff"
}
else if (room_picking == 4) {
    document.getElementById("task4.2").innerText = "Ravenclaw"
}