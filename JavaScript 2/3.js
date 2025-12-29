const dogs = []

while (dogs.length < 6) {
    dogs.push(prompt("Enter the name of dog " + `${dogs.length + 1}` + ": "))
}

dogs.sort().reverse()

document.getElementById("dog_list").innerText = dogs