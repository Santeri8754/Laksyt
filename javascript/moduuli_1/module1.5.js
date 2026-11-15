'use strict';
let vuosi = parseInt(prompt("Anna vuosi: "));

let vastaus =document.querySelector('#vastaus');

if((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0)){
    //On karkausvuosi
    vastaus.innerHTML = `${vuosi} on karkausvuosi`;
}
else{
    // Ei ole karkausvuosi
    vastaus.innerHTML = `${vuosi} ei ole karkausvuosi`;
}