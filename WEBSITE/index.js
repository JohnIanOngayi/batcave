/*TYPE CONVERSIONS*/
let age = window.prompt("How old are you");
console.log(`${typeof age}`);
//Use Number Function to convert to integer
age = Number(age);
console.log(`${typeof age}`);
console.log(`${age}`);
/*
 * Other type converter functions include
 *  - String()
 *  - Boolean()
 *      As long as there's some value Boolean returns true
 *      A typical usecase for this would be to check whether user
 *      added input required
 * */
