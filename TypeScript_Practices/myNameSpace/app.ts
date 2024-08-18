/// <reference path='./app2.ts' />
namespace usersUtils {
  export class Users extends Parent {
    getname() {
      return "I am a user";
    }
  }
}
let u1 = new usersUtils.Users();
console.log(u1.getname());
console.log(u1.getstatus());
