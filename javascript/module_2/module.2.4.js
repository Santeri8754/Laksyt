'use strict'

const luvut = []
let luku = parseInt(prompt("Anna luku (0 lopettaa): "))
while (luku !== 0){
    luvut.push(luku);
    luku=parseInt(prompt("Anna luku (0 lopettaa): "))
}
luvut.sort((a,b) => a-b)

for(const n of luvut){
    console.log(n);
}