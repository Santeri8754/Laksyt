'use strict';

let alku= parseInt(prompt("Anna alkuvuosi "));
let loppu= parseInt(prompt("Anna loppuvuosi "));

let lista =document.getElementById('lista');

for (let v=alku; v<=loppu;v +=1)
{

    if((v % 4 === 0 && v % 100 !== 0) || (v % 400 === 0)){
        lista.innerHTML += `<li>${v}</li>`;
    }

}