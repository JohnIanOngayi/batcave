/*
 * TEMP CONVERTER
 */
const toFahren = document.getElementById("radio-c");
const toCelsiu = document.getElementById("radio-f");
const btn = document.getElementById("btn-submit");
const result = document.getElementById("result");

btn.onclick = function () {
  event.preventDefault();
  const input = Number(document.getElementById("input-bar").value);
  if (toFahren.checked) {
    result.textContent = (input * 9) / 5 + 32;
  } else if (toCelsiu.checked) {
    result.textContent = (input * 5) / 9 - 32;
  } else {
    result.textContent = "Nuuh";
  }
};
