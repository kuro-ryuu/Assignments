let hover = document.getElementById("trigger")
let target = document.getElementById("target")


hover.addEventListener("mouseover", () => {
    target.src = "img/picB.jpg"
})
hover.addEventListener("mouseout", () => {
    target.src = "img/picA.jpg"
})


