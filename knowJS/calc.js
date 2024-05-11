// function printSymbol(e) {
//   let result = document.getElementById("result");
//   let obj = e.target;
//   result.textContent += obj.textContent;
// }
// function clearResult() {
//   let result = document.getElementById("result");
//   result.textContent = "";
// }

const printSymbol = (e) => {
  result.textContent += e.target.textContent;
};
//
// const clearResult = () => {
//   result.textContent = "";
// };

let result = document.getElementById("result");
const num0 = document.getElementById("num0");
const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const num3 = document.getElementById("num3");
const num4 = document.getElementById("num4");
const num5 = document.getElementById("num5");
const num6 = document.getElementById("num6");
const num7 = document.getElementById("num7");
const num8 = document.getElementById("num8");
const num9 = document.getElementById("num9");
const AC = document.getElementById("clear");
const add = document.getElementById("add");
const add2 = document.getElementById("add2");
const perc = document.getElementById("perc");
const div = document.getElementById("div");
const mul = document.getElementById("mul");
const pt = document.getElementById("pt");
const eq = document.getElementById("eq");

num0.addEventListener("click", printSymbol);
num1.addEventListener("click", printSymbol);
num2.addEventListener("click", printSymbol);
num3.addEventListener("click", printSymbol);
num4.addEventListener("click", printSymbol);
num5.addEventListener("click", printSymbol);
num6.addEventListener("click", printSymbol);
num7.addEventListener("click", printSymbol);
num8.addEventListener("click", printSymbol);
num9.addEventListener("click", printSymbol);
add.addEventListener("click", printSymbol);
add2.addEventListener("click", printSymbol);
perc.addEventListener("click", printSymbol);
div.addEventListener("click", printSymbol);
mul.addEventListener("click", printSymbol);
pt.addEventListener("click", printSymbol);
AC.addEventListener("click", () => (result.textContent = ""));
