'use strict';

const form = document.querySelector("#searchForm");
const queryInput = document.getElementById("query");

form.addEventListener("submit", function (event) {
    event.preventDefault();

const query = queryInput.value;

fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
    .then(response => response.json())
    .then(data => {
        const formattedJson = JSON.stringify(data, null, 2);
            document.getElementById("results").innerHTML = `<pre>${formattedJson}</pre>`;
            console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

