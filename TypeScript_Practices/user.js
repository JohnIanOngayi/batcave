#!/usr/bin/node
"use strict";
let nextUserId = 1;
const users = [
    { id: nextUserId++, username: "john doe", role: "member" },
    { id: nextUserId++, username: "jane doe", role: "contributor" },
    { id: nextUserId++, username: "alice jones", role: "admin" },
    { id: nextUserId++, username: "charlie brown", role: "member" },
];
function addNewUser(newUser) {
    if (!newUser.username || !newUser.role) {
        throw new Error("User must have a username and role");
    }
    if (!["member", "contributor", "admin"].includes(newUser.role)) {
        throw new Error("Invalid role");
    }
    const user = Object.assign({ id: nextUserId++, username: "", role: "member" }, newUser);
    users.push(user);
    return user;
}
// interface Dictionary<T> {
//   [key: string]: T;
// }
//
// function updateUser(id: number, updates: Dictionary<any>): User | never {
//   const usr = users.find((value) => value.id === id);
//   if (usr) {
//     for (const key in updates) {
//       usr[key] = updates[key];
//     }
//     return usr;
//   }
//   throw new Error(`User id: ${id} does not exist`);
// }
function updateUser(id, updates) {
    const usr = users.find((user) => user.id === id);
    if (usr) {
        Object.assign(usr, updates);
        return usr;
    }
    throw new Error(`User id: ${id} is non-existent`);
}
console.log(users);
console.log(updateUser(2, { username: "new jane doe", age: 25, password: "booyah" }));
addNewUser({ username: "james bond", role: "member", height: "6ft2in" });
console.log(users);
