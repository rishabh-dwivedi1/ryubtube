console.log("Ryutube Loaded Successfully");


// Navbar shadow on scroll

window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 10) {
        navbar.style.boxShadow = "0 2px 10px rgba(255,0,0,0.5)";
    } else {
        navbar.style.boxShadow = "none";
    }

});


// Video card hover animation

const videoCards = document.querySelectorAll(".video-card");

videoCards.forEach(card => {

    card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.03)";
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });

});


// Search input animation

const searchInput = document.querySelector("input[name='q']");

if (searchInput) {

    searchInput.addEventListener("focus", () => {
        searchInput.style.border = "1px solid red";
    });

    searchInput.addEventListener("blur", () => {
        searchInput.style.border = "1px solid #444";
    });

}


// Upload success alert

const uploadForm = document.querySelector("form");

if (uploadForm && window.location.pathname.includes("upload")) {

    uploadForm.addEventListener("submit", () => {

        alert("Video Upload Started!");

    });

}