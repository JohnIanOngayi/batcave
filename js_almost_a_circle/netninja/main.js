#!/usr/bin/env node

// var userOne = {
//   email: "ryu@ninjas.com",
//   name: "ryu",
//   login() {
//     console.log(`${this.name} is logged in!`);
//   },
//   logout() {
//     console.log(`${this.email} has logged out!`);
//   },
// };
//
// userOne["age"] = 26;
// console.log(userOne);

// class User {
//   #nb_objects = 0;
//   constructor(email, name) {
//     this.email = email;
//     this.name = name;
//   }
//   login() {
//     console.log(`User ${this.name} with email ${this.email} logged in!`);
//     return this;
//   }
//   logout() {
//     console.log(`User ${this.name} logged out!`);
//     return this;
//   }
// }
//
// class Admin extends User {
//   deleteUser(user) {
//     users = users.filter((u) => {
//       return u != user;
//     });
//   }
// }
function User(email, name) {
  this.email = email;
  this.name = name;
  this.online = false;
}

User.prototype.login = function () {
  this.online = true;
  console.log(`${this.name} logged in with ${this.email}!`);
};
User.prototype.logout = function () {
  this.online = false;
  console.log(`${this.name} logged out!`);
};

function Admin(...args) {
  User.apply(this, args);
}
Admin.prototype.deleteUser = function (user) {
  users = users.filter((value) => {
    return value != user;
  });
};

ian = new User("ian@greenumco.com", "ian");
ryu = new User("ryu@ninjas.com", "ryu");
rcn = new Admin("rcn@greenumco.com", "rcn");
console.log(rcn);
var users = [ian, ryu];
console.log(users);
rcn.deleteUser(ryu);
console.log(users);
