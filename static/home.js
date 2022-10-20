let img = document.getElementById('img');
let video = document.getElementById('video');
let box1 = document.getElementById('box1');
let box2 = document.getElementById('box2');
let box3 = document.getElementById('box3');

let s1 = document.getElementById('s1');
let s2 = document.getElementById('s2');
let s3 = document.getElementById('s3');
let s4 = document.getElementById('s4');

/* window.onload = function () {
    setInterval(count, 6000);
};

function count() {
    plusSlides1(1, 0)
} */


window.addEventListener('scroll', function () {
    let value = window.scrollY;
    logo.style.bottom = (value * 2) + 'px';

    if (value >= 800) {
        img.style.bottom = value * -0.6 + 'px';
        video.style.bottom = value * -0.6 + 'px';
    }
    else {
        img.style.top = value * 0.6 + 'px';
        video.style.top = value * 0.6 + 'px';
    }

    if (value >= 300) {
        move = -120 + (value * 0.4);
        box1.style.transform = "translateX(" + move + "px)";
        box2.style.left = -60 + (value * 0.2) + 'px';
        box3.style.left = -30 + (value * 0.1) + 'px';
    }

    if (value >= 200 && value <= 1000) {
        s1.style.right = -800 + (value * 0.8) + 'px';
        s2.style.right = -800 + (value * 0.8) + 'px';
        s3.style.right = -800 + (value * 0.8) + 'px';
        s4.style.right = -800 + (value * 0.8) + 'px';
    }

})

window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if ((document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) && window.innerWidth > 1300) {
        document.getElementById("header").style.height = "4vw";
        document.getElementById("align").style.display = "none";
        document.getElementById("logo").style.width = "30%";
        document.getElementById("burger").style.display = "inherit";
        document.getElementById("menu").style.display = "inherit";
        document.getElementById("logo").style.marginLeft = "34%";
        document.getElementById("bottom-bar").style.display = "inherit";
    } else {
        document.getElementById("logo").style.marginLeft = "31.2%";
        document.getElementById("align").style.display = "inherit";
        document.getElementById("logo").style.width = "35%";
        document.getElementById("header").style.height = "12%";
        document.getElementById("burger").style.display = "none";
        document.getElementById("menu").style.display = "none";
        document.getElementById("bottom-bar").style.display = "none";
    }
}

window.addEventListener('resize', function () {
    if (window.innerWidth <= 1300) {
        document.getElementById("header").style.height = "5%";
        document.getElementById("m").style.display = "inherit";
        document.getElementById("arrow").style.display = "none";
        document.getElementById("logoBig").style.display = "inherit";
        document.getElementById("rooms-showcase-small").style.display = "block";
        document.getElementById("rooms-showcase-large").style.display = "none";
        document.getElementById("lines").style.display = "none";
        document.getElementById("button").style.display = "none";
    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth < 800) {
        document.getElementById("bottom-bar").style.display = "none";
        document.getElementById("lines").style.display = "none";
    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth < 650) {
        document.getElementById("back-video").style.width = "270%";
        document.getElementById("main-slideshow").style.width = "270%";
        document.getElementById("lines").style.display = "none";
    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth >= 1300) {
        document.getElementById("header").style.height = "12%";
        document.getElementById("m").style.display = "none";
        document.getElementById("arrow").style.display = "inherit";
        document.getElementById("logoBig").style.display = "none";
        document.getElementById("rooms-showcase-small").style.display = "none";
        document.getElementById("rooms-showcase-large").style.display = "inherit";
        document.getElementById("rooms-showcase-large").style.flexDirection = "row";
        document.getElementById("rooms-showcase-large").style.display = "flex";
        document.getElementById("main-slideshow").style.width = "90%";
        document.getElementById("lines").style.display = "flex";
        document.getElementById("button").style.display = "flex";

    }
})

window.addEventListener('resize', function () {
    if (window.innerWidth > 800) {
        document.getElementById("bottom-bar").style.display = "inherit";
        document.getElementById("lines").style.display = "inherit";
    }
})

window.addEventListener('resize', function () {
    if ((window.innerWidth >= 650) && (window.innerWidth < 1300)) {
        document.getElementById("back-video").style.width = "100%";
        document.getElementById("main-slideshow").style.width = "100%";
    }
})

window.addEventListener('scroll', function () {
    if (window.innerWidth < 1300) {
        document.getElementById("header").style.height = "5%";
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

