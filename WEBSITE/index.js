/*
 * PASSWORD GENERATOR
 */

function generatePasswd(
  passwdLength,
  includeLowercase,
  includeUppercase,
  includeNumbers,
  includeSymbols,
) {
  const lowercase = "abcdefghijklmnopqrstuvwxyz";
  const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numbers = "0123456789";
  const symbols = "!@#$%^&*_-<,.>";
  let random_set;
  let random_char;
  let passwd = "";

  let selectable_setofChars = [];
  if (includeLowercase) {
    selectable_setofChars.push(lowercase);
  }
  if (includeUppercase) {
    selectable_setofChars.push(uppercase);
  }
  if (includeNumbers) {
    selectable_setofChars.push(numbers);
  }
  if (includeSymbols) {
    selectable_setofChars.push(symbols);
  }
  if (passwdLength < 1) {
    return "Password length has to be at least 1";
  }
  if (selectable_setofChars.length == 0) {
    return "You have to select at least a set of characters";
  }

  for (let i = 0; i < passwdLength; i++) {
    random_set = Math.floor(Math.random() * selectable_setofChars.length);
    random_char = Math.floor(
      Math.random() * selectable_setofChars[random_set].length,
    );
    passwd += selectable_setofChars[random_set][random_char];
  }
  return passwd;
}
const btn = document.getElementById("btn-submit");
btn.onclick = function () {
  event.preventDefault();
  const passwdLength = document.getElementById("length").value;
  const includeLowercase = Boolean(
    document.getElementById("lowercase").checked,
  );
  const includeUppercase = Boolean(
    document.getElementById("uppercase").checked,
  );
  const includeNumbers = Boolean(document.getElementById("numbers").checked);
  const includeSymbols = Boolean(document.getElementById("symbols").checked);
  const generated = generatePasswd(
    passwdLength,
    includeLowercase,
    includeUppercase,
    includeNumbers,
    includeSymbols,
  );
  document.getElementById("holder-text").textContent = "Generated Passcode";
  document.getElementById("result").textContent = generated;
};
