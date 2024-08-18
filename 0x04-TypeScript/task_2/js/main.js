#!/usr/bin/node
var Director = /** @class */ (function () {
    function Director() {
        this.workFromHome = function () {
            return "Working from home";
        };
        this.getCoffeeBreak = function () {
            return "Getting a coffee break";
        };
        this.workDirectorTasks = function () {
            return "Getting to director tasks";
        };
    }
    return Director;
}());
var Teacher = /** @class */ (function () {
    function Teacher() {
        this.workFromHome = function () {
            return "Cannot work from home";
        };
        this.getCoffeeBreak = function () {
            return "Cannot have a break";
        };
        this.workTeacherTasks = function () {
            return "Getting to work";
        };
    }
    return Teacher;
}());
/**
 * creates a Teacher or Director objects
 *
 * @param salary salary of the teacher or director
 * @returns Teacher or Director object
 */
function createEmployee(salary) {
    if (typeof salary === "number") {
        return salary <= 500 ? new Teacher() : new Director();
    }
    else
        throw new Error("Salary must be an integer");
}
/**
 * type predicate checks if employee is Teacher or Director
 *
 * @param employee the employee to check
 * @returns True if Director
 */
function isDirector(employee) {
    return employee instanceof Director;
}
/**
 * calls function that returns employee tasks
 *
 * @param employee the employee to be assigned tasks
 * @returns  string
 */
function executeWork(employee) {
    if (employee instanceof Director) {
        return employee.workDirectorTasks();
    }
    else {
        return employee.workTeacherTasks();
    }
}
/**
 * tells current class
 *
 * @param todayClass today's subject
 * @returns string says which class to be taught today
 */
function teachClass(todayClass) {
    return "Teaching ".concat(todayClass);
}
// console.log(createEmployee(200));
// console.log(createEmployee(1500));
// console.log(executeWork(createEmployee(50)));
// console.log(executeWork(createEmployee(1500)));
console.log(teachClass("Math"));
console.log(teachClass("History"));
