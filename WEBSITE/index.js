/*
 * A counter program
 * */
let number = 0;

document.getElementById("decr").onclick = function () {
  number -= 1;
  document.getElementById("digit_header").textContent = number;
};

document.getElementById("incr").onclick = function () {
  number += 1;
  document.getElementById("digit_header").textContent = number;
};

document.getElementById("reset").onclick = function () {
  number = 0;
  document.getElementById("digit_header").textContent = number;
};
/*
 * what would have been easier would be fetching by id and storing in const's
 *  - const decr = document.getElementById("decr")
 *  - const incr = document.getElementById("incr")
 *  - const reset = document.getElementById("reset")
 * */
