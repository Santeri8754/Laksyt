const nimi = prompt("Anna nimesi: ")
const randomNum= Math.floor(Math.random()*4)+1;
let house=""

if(randomNum ===1){

    house="Gryffindor"
}
else if(randomNum === 2){
    house="Slytherin"
}
else if(randomNum === 3){
    house="Hufflepuff"
}
else {
    house="Ravenclaw"
}

document.querySelector("#tulokset").innerText=nimi + " , you are " + house;