//Event handlers for highlight element
const hypothesis = document.getElementById("hypothesis")
const analysis = document.getElementById("analysis")

hypothesis.addEventListener("mouseover", function() {
    hypothesis.style.backgroundColor = "#7bbf7b";;
});

hypothesis.addEventListener("mouseout", function() {
    hypothesis.style.backgroundColor = "#ffffff";;
});

analysis.addEventListener("mouseover", function() {
    analysis.style.backgroundColor = "#7bbf7b";;
});

analysis.addEventListener("mouseout", function() {
    analysis.style.backgroundColor = "#ffffff";;
});

//Event handlers for click change element
hypothesis.addEventListener("click", function() {
    hypothesis.style.display = "none";
    analysis.style.display = "block";
});

analysis.addEventListener("click", function() {
    analysis.style.display = "none";
    hypothesis.style.display = "block";
});