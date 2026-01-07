'use strict';

const form = document.getElementById("searchForm");
const queryInput = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const query = queryInput.value;
    resultsDiv.innerHTML = "";

    try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${query}`
    );

    const data = await response.json();

    data.forEach(item => {
        const show = item.show;

        const article = document.createElement("article");

        const title = document.createElement("h2");
        title.textContent = show.name;

        const link = document.createElement("a");
        link.href = show.url;
        link.target = "_blank";
        link.textContent = "View details";

        const img = document.createElement("img");
        img.src = show.image
        if (show.image.medium)
            img.src = show.image.medium
        else
            img.src = "https://via.placeholder.com/210x295?text=Not%20Found";
        img.alt = show.name;

        const summary = document.createElement("div");
        summary.innerHTML = show.summary || "No summary available.";

        article.append(title, link, img, summary);
        resultsDiv.appendChild(article);
    });

    } catch (error) {
    console.error("Fetch failed:", error);
    }
});
