function over(element) {
    element.style.color = "blue";
}

function out(element) {
    element.style.color = "white";
}

function hover(element) {
    element.style.color = "black";
}

function end_hover(element) {
    element.style.color = "white";
}

function link(element) {
    element.style.color = "blue";
    element.style.textDecoration = "underline";
}

function unlink(element) {
    element.style.color = "white";
    element.style.textDecoration = "none";
}

function oncar(element) {
    element.style.backgroundColor = "silver";
}

function offcar(element) {
    element.style.backgroundColor = "grey";
}

function review(element) {
    element.style.backgroundColor = "skyblue";
}

function outreview(element) {
    element.style.backgroundColor = "blue";
}

function onlink(element) {
    element.style.color = "blue";
    element.style.textDecoration = "underline";
}
function offlink(element) {
    element.style.color = "white";
    element.style.textDecoration = "none";
}

function onvehicle(element) {
    element.style.color = "white";
    element.style.textDecoration = "underline";
}

function offvehicle(element) {
    element.style.color = "white";
    element.style.textDecoration = "none";
}

function onbtn(element) {
    element.style.backgroundColor = "blue";
}

function offbtn(element) {
    element.style.backgroundColor = "white";
}

function offthisbtn(element) {
    element.style.backgroundColor = "rgb(37, 118, 211)";
}
//PopUp Function
function togglePopup() {
    document.getElementById('popup-1').classList.toggle('active');
}

function loginPopup() {
    document.getElementById('popup-2').classList.toggle('active');
}

function playVideo (vid){
    console.log(vid);
    vid.play();
}

function pauseVideo (vid){
    console.log(vid);
    vid.pause();
}

//Live Chat

$crisp.push(['do', 'chat:open']);


