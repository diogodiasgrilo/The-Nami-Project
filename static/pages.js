window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if ((document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) && window.innerWidth > 1300) {
        document.getElementById("header").style.height = "4vw";
        document.getElementById("align").style.display = "none";
        document.getElementById("logo").style.width = "30%";
        document.getElementById("burger").style.display = "inherit";
        document.getElementById("menu").style.display = "inherit";
        document.getElementById("logo").style.marginLeft = "34%";
    } else {
        document.getElementById("logo").style.marginLeft = "31.2%";
        document.getElementById("align").style.display = "inherit";
        document.getElementById("logo").style.width = "35%";
        document.getElementById("header").style.height = "12%";
        document.getElementById("burger").style.display = "none";
        document.getElementById("menu").style.display = "none";
    }

    if ((document.body.scrollTop > 58 || document.documentElement.scrollTop > 58) && window.innerWidth > 1300) {
        document.getElementById("bottom-bar").style.display = "inherit";
    } else {
        document.getElementById("bottom-bar").style.display = "none";
    }
}


window.addEventListener('resize', function () {
    if (window.innerWidth >= 1300) {
        document.getElementById("header").style.height = "12%";
        document.getElementById("m").style.display = "none";
    }
})


window.addEventListener('resize', function () {
    if (window.innerWidth > 800) {
        document.getElementById("bottom-bar").style.display = "inherit";
    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth <= 1300) {
        document.getElementById("header").style.height = "5%";
        document.getElementById("m").style.display = "inherit";
    }
})

window.addEventListener('scroll', function () {
    if (window.innerWidth < 1300) {
        document.getElementById("header").style.height = "5%";
    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth < 800) {
        document.getElementById("bottom-bar").style.display = "none";
    }
})


let slideIndex1 = 1;

// Next/previous controls
function plusSlides1(n, x) {
    showSlides1((slideIndex1 += n), x);
}

// Thumbnail image controls
function currentSlide1(n) {
    showSlides1(slideIndex1 = n);
}

function showSlides1(n, x) {
    let i;
    if (x == 0) {
        let slides = document.getElementsByClassName("mySlides0");
        if (n > slides.length) { slideIndex1 = 1 }
        if (n < 1) { slideIndex1 = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex1 - 1].style.display = "block";
    } else if (x == 1) {
        let slides = document.getElementsByClassName("mySlides1");
        if (n > slides.length) { slideIndex1 = 1 }
        if (n < 1) { slideIndex1 = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex1 - 1].style.display = "block";
    } else if (x == 2) {
        let slides = document.getElementsByClassName("mySlides2");
        if (n > slides.length) { slideIndex1 = 1 }
        if (n < 1) { slideIndex1 = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex1 - 1].style.display = "block";
    } else if (x == 3) {
        let slides = document.getElementsByClassName("mySlides3");
        if (n > slides.length) { slideIndex1 = 1 }
        if (n < 1) { slideIndex1 = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex1 - 1].style.display = "block";
    } else if (x == 6) {
        let slides = document.getElementsByClassName("mySlides6");
        if (n > slides.length) { slideIndex1 = 1 }
        if (n < 1) { slideIndex1 = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex1 - 1].style.display = "block";
    }
}
