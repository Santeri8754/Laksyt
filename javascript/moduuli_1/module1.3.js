const num1= parseInt(prompt("Anna luku1: "))
const num2= parseInt(prompt("Anna luku2: "))
const num3= parseInt(prompt("Anna luku3: "))

const summa= num1 + num2 + num3;
const kerto=num1* num2 * num3;
const keski= summa/3;

document.querySelector("#kohde").innerHTML=
    "Summa: " + summa +"<br>"+
    "Kerto: " + kerto +"<br>" +
    "Keskiarvo: " + keski;

