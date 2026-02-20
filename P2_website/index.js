//Event handlers for highlight element
const stateOne = document.getElementById("stateOne")
const stateTwo = document.getElementById("stateTwo")

stateOne.addEventListener("mouseover", function() {
    stateOne.style.backgroundColor = "#a7e6a7";;
});

stateOne.addEventListener("mouseout", function() {
    stateOne.style.backgroundColor = "#ffffff";;
});

stateTwo.addEventListener("mouseover", function() {
    stateTwo.style.backgroundColor = "#a7e6a7";;
});

stateTwo.addEventListener("mouseout", function() {
    stateTwo.style.backgroundColor = "#ffffff";;
});

//Event handlers for click change element
stateOne.addEventListener("click", function() {
    stateOne.style.display = "none";
    stateTwo.style.display = "block";
});

stateTwo.addEventListener("click", function() {
    stateTwo.style.display = "none";
    stateOne.style.display = "block";
});

//Event handlers for highlight element
const methodology = document.getElementById("methodology")
const limitations = document.getElementById("limitations")

methodology.addEventListener("mouseover", function() {
    methodology.style.backgroundColor = "#a7e6a7";;
});

methodology.addEventListener("mouseout", function() {
    methodology.style.backgroundColor = "#ffffff";;
});

limitations.addEventListener("mouseover", function() {
    limitations.style.backgroundColor = "#a7e6a7";;
});

limitations.addEventListener("mouseout", function() {
    limitations.style.backgroundColor = "#ffffff";;
});

//Event handlers for click change element
methodology.addEventListener("click", function() {
    methodology.style.display = "none";
    limitations.style.display = "block";
});

limitations.addEventListener("click", function() {
    limitations.style.display = "none";
    methodology.style.display = "block";
});

