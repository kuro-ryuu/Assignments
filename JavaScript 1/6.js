document.getElementById("task6.1").innerHTML = "<h3>Task 6 result: </h3>";

const sqrtCalc = confirm("woud yuo caclate a sqrotoot? 🥺 <- pleading eyes emoij")

if (sqrtCalc == true) {
    const num = prompt("okay!!!!!! nombor pleas!!!!!??!?")
    if (num < 0) {
        document.getElementById("task6.2").innerText = "nincompoop behavior"
    }
    else if (num == "") {
        document.getElementById("task6.2").innerText = "coulda just say cancel but okay"
    }
    else
        document.getElementById("task6.2").innerText = "oka so ur quoot of " + num + " is like something something " + num**0.5
}
else {
    document.getElementById("task6.2").innerText = "oka, it's not like i need ur nombor and them calculations or anything. Have fun with ur empty void of no square roots"
}