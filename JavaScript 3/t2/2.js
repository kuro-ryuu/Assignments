const list2 = document.getElementById("target");

const item1 = document.createElement("li");
item1.textContent = "First item";

const item2 = document.createElement("li");
item2.textContent = "Second item";
item2.classList.add("my-item");

const item3 = document.createElement("li");
item3.textContent = "Third item";

list2.appendChild(item1);
list2.appendChild(item2);
list2.appendChild(item3);