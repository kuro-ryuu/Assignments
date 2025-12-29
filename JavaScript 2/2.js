const participants = []

no_of_participants = Number(prompt("Enter the number of participants: "))

for (let i = 0; i < no_of_participants; i++) {
    participants[i] = prompt("Enter the name of participant " + `${i+1}` + ": ")
        participants.push(participants)
}

participants.sort()

document.getElementById('participant_list').innerText = participants