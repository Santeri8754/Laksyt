'use strict'

const trigger = document.querySelector("#trigger")
const target = document.querySelector("#target")

trigger.addEventListener("mouseover",function() {
    target.src ='img/picB.jpg'
})

target.addEventListener("mouseover",function() {
    target.src ='img/picA.jpg'
})