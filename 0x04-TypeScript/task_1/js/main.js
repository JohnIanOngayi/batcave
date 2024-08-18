#!/usr/bin/node
var StudentClass = /** @class */ (function () {
    function StudentClass(firstName, lastName) {
        var _this = this;
        this.workOnHomework = function () {
            return "Currently working";
        };
        this.displayName = function () {
            return _this.firstName;
        };
        this.lastName = lastName;
        this.firstName = firstName;
    }
    return StudentClass;
}());
/**
 * function prints shortened name of teacher
 *
 * @param {string} firstName  first name of Teacher
 * @param {string} lastName  last name of Teacher
 * @returns {string}  1st character from first name and last name
 */
var printTeacherFunction = function (firstName, lastName) {
    return "".concat(firstName.charAt(0), ", ").concat(lastName);
};
// Create a Teacher object with required and additional properties
var teacher3 = {
    firstName: "John",
    fullTimeEmployee: false,
    lastName: "Doe",
    location: "London",
    contract: false,
};
// Log the Teacher object to the console
// console.log(teacher3);
// console.log(printTeacherFunction(teacher3.firstName, teacher3.lastName));
// Create a Directors object with required properties from Teacher and Directors
var director1 = {
    firstName: "John",
    lastName: "Doe",
    location: "London",
    fullTimeEmployee: true,
    numberOfReports: 17,
};
var student1 = new StudentClass("Charlie", "Brown");
// Log the Directors object to the console
// console.log(director1);
console.log("Student1: ", student1);
console.log(student1.workOnHomework());
console.log(student1.displayName());
