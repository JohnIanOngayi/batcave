/*
 * Strict Equality Operators
 * == comparison operator(values equal?)
 * === strict equality operator(values and data types equal)
 * != inequality operator
 * !== strict inequality operator
 * = assignment operator
 */
const PI = 3.14;

if (PI == "3.14") {
  console.log("That is PI");
} else {
  console.log("That isn't PI");
}

if (PI === "3.14") {
  console.log("That is exactly PI");
} else {
  console.log("That isn't exactly PI");
}
