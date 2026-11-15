const koirat=[]

for(let i = 0; i < 6; i++){

    const nimi = prompt(`Anna koiran nimi ${i+ 1} `);
    koirat.push(nimi);
}
koirat.sort()
koirat.reverse()

const kohde =document.querySelector("#kohde");
for ( const koira of koirat){
    kohde.innerHTML += `<li>${koira}</li>`;
}