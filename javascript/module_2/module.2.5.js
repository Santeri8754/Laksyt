const luvut= []

while(true){
    let luku = parseInt(prompt("Anna luku: "))

    if(luvut.includes(luku)){
        console.log(`luku ${luku} on jo annettu!!`)
        break
    }

    if(!isNaN(luku)){
        luvut.push(luku)
    }

}
luvut.sort((a, b) => a - b)

for (const n  of luvut){
    console.log(n)
}