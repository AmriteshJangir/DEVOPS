// Add event listeners to buttons
document.getElementById("devops-btn").addEventListener("click", function() {
    var content = document.getElementById("devops-content");
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
});

document.getElementById("pipeline-btn").addEventListener("click", function() {
    var content = document.getElementById("pipeline-content");
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
});

document.getElementById("benefits-btn").addEventListener("click", function() {
    var content = document.getElementById("benefits-content");
    if (content.style.display === "none") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
});

document.getElementById("tools-btn").addEventListener("click", function() {
    var content = document.getElementById("tools-content");