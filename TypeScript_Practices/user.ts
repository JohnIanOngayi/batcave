#!/usr/bin/node

let nextUserId: number = 1;

type User = {
  id: number;
  username: string;
  role: "member" | "contributor" | "admin";
  [key: string]: any;
};

const users: Array<User> = [
  { id: nextUserId++, username: "john doe", role: "member" },
  { id: nextUserId++, username: "jane doe", role: "contributor" },
  { id: nextUserId++, username: "alice jones", role: "admin" },
  { id: nextUserId++, username: "charlie brown", role: "member" },
];

/**
 * Adds a new user to the system.
 *
 * @param newUser - An object containing the new user's details, excluding the `id` field.
 * @returns The newly created user object with an `id` field.
 * @throws Will throw an error if the `username` or `role` is missing.
 * @throws Will throw an error if the `role` is not one of "member", "contributor", or "admin".
 */
function addNewUser(newUser: Omit<User, "id">): User | never {
  if (!newUser.username || !newUser.role) {
    throw new Error("User must have a username and role");
  }
  if (!["member", "contributor", "admin"].includes(newUser.role)) {
    throw new Error("Invalid role");
  }
  const user: User = {
    id: nextUserId++,
    username: "",
    role: "member",
    ...newUser,
  };
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
function updateUser(id: number, updates: unknown): User | never {
  const usr = users.find((user) => user.id === id);
  if (usr) {
    Object.assign(usr, updates);
    return usr;
  }
  throw new Error(`User id: ${id} is non-existent`);
}

console.log(users);
console.log(
  updateUser(2, { username: "new jane doe", age: 25, password: "booyah" }),
);
addNewUser({ username: "james bond", role: "member", height: "6ft2in" });
console.log(users);
