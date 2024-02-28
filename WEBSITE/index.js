/*
 * Using if statements to lock youngins out
 */
let age = document.getElementById("usrname_age").value;
document.getElementById("btn_submit").onclick = function () {
  if (Number(age) < 18) {
    window.alert("access denied");
  } else {
    window.alert("Welcome");
  }
};
