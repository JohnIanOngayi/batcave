#!/usr/bin/node

/*
const astr = "4155049898"
const bstr ="' 4155049898 '"
const cstr ="'415 504 9898'"
const dstr ="'415-504-9898'"
const myreg = /\S[0-9]{10}\S/g
console.log(astr.match(myreg))
console.log(myreg.test(astr))
*/

const mystr = "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream"
const myreg = /[A-Z]/g
console.log(join(mystr.match(myreg)))
