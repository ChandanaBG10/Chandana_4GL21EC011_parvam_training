const header=document.querySelector("header");

window.addEventListener("scroll",function(){
    header.classList.toggle ("sticky",this.window. scrollY> 0);
});
let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onClick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.open('bx-x');
}

menu.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('bx-x');
}

