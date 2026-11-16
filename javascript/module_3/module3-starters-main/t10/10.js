'use strict'

const form=document.querySelector('form')
const firstNameInput=document.querySelector('input[name="firstname"]')
const lastNameInput=document.querySelector('input[name="lastname"]')
const target= document.querySelector('#target')

form.addEventListener('submit', function(event) {
    event.preventDefault()
    const firstname = firstNameInput.value
    const lastName = lastNameInput.value
    target.textContent = `Your name is ${firstname} ${lastName}`
})