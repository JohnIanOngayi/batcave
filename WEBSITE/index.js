/*
 * THE Math OBJECT
 *
 * Does a bunch of math operations
 */
let a = 6;
let b = 4;
let c = 1;
let d = 3.26;
let e = -2.51;
let z;

let PI = Math.PI;
let E = Math.E;
z = Math.round(d);
z = Math.floor(d);
z = Math.ceil(d);
z = Math.trunc(d);
z = Math.pow(a, b);
z = Math.sqrt(a);
z = Math.log(d);
z = Math.sin(c);
z = Math.cos(d);
z = Math.tan(d);
z = Math.abs(d);
z = Math.sign(e);

/*
 * RANDOM NUMBER GENERATOR WEBSITE FOR ROLLING A SIX-SIDED DICE
 *    using the Math object
 */
const generate = document.getElementById("generate");
const number = document.getElementById("digit_header");
generate.onclick = function () {
  let myRandom = Math.floor(Math.random() * 6) + 1;
  number.textContent = myRandom;
};
/*
 * The Math.random() returns a long decimal value between 0 and 1
 * Say I want a range between max and min
 * myRandomNum = Math.floor(Math.random() * (max - min)) + min
 */
