const maara= parseInt(prompt("Anna osallistujien määrä: "))

const osallistujat = []
for(let i = 0; i < maara; i++){

    const nimi = prompt(`Anna  ${i+ 1} osallistuan nimi:`);
    osallistujat.push(nimi);
}
osallistujat.sort()

const lista =document.querySelector("#target");
for ( const nimi of osallistujat){
    lista.innerHTML += `<li>${nimi}</li>`;
}