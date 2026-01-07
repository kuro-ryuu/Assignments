const jokeList = document.getElementById('joke');
const jokeForm = document.getElementById('chuckNorris');

jokeForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const searchInput = document.getElementById('jokeInput');
    const searchQuery = searchInput.value;
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${searchQuery}`);
    const jokes = await response.json();
    jokeList.innerHTML = '';
    jokes.result.forEach(joke => {
    const jokeItem = document.createElement('p');
    jokeItem.textContent = joke.value;
    jokeList.appendChild(jokeItem);
    });
});