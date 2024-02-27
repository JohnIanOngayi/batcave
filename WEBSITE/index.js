//window.alert(`This is an alert`);
//window.alert(`Stop It Now!`);
//"Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.";
let age = 26;
let name = "Dimmz";
////document.getElementById("main_header").textContent = name;
////document.getElementById("lorem").textContent = name;
let online = true;
console.log(`${age}`);
console.log(typeof age);
console.log(`First name ${name} is of type ${typeof name}`);
console.log(`Variable ${online} is of type ${typeof online}`);
console.log(`${age * 2}`);
document.getElementById("submit_usr_name").onclick = function () {
  let username = document.getElementById("fetch").value;
  document.getElementById("main_header").textContent = `Hello ${username}`;
  console.log(`Backtickling ${username}`);
};
