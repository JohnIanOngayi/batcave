#!/usr/bin/node

interface TeacherFn {
  (): string;
}

interface DirectorInterface {
  workFromHome: TeacherFn;
  getCoffeeBreak: TeacherFn;
  workDirectorTasks: TeacherFn;
}

interface TeacherInterface {
  workFromHome: TeacherFn;
  getCoffeeBreak: TeacherFn;
  workTeacherTasks: TeacherFn;
}

class Director implements DirectorInterface {
  workFromHome: TeacherFn = () => {
    return "Working from home";
  };
  getCoffeeBreak: TeacherFn = () => {
    return "Getting a coffee break";
  };
  workDirectorTasks: TeacherFn = () => {
    return "Getting to director tasks";
  };
}

class Teacher implements TeacherInterface {
  workFromHome: TeacherFn = () => {
    return "Cannot work from home";
  };
  getCoffeeBreak: TeacherFn = () => {
    return "Cannot have a break";
  };
  workTeacherTasks: TeacherFn = () => {
    return "Getting to work";
  };
}

/**
 * creates a Teacher or Director objects
 *
 * @param salary salary of the teacher or director
 * @returns Teacher or Director object
 */
function createEmployee(salary: number | string): Teacher | Director {
  if (typeof salary === "number") {
    return salary <= 500 ? new Teacher() : new Director();
  } else throw new Error("Salary must be an integer");
}

/**
 * type predicate checks if employee is Teacher or Director
 *
 * @param employee the employee to check
 * @returns True if Director
 */
function isDirector(employee: Teacher | Director): boolean {
  return employee instanceof Director;
}

/**
 * calls function that returns employee tasks
 *
 * @param employee the employee to be assigned tasks
 * @returns  string
 */
function executeWork(employee: Teacher | Director): string {
  if (employee instanceof Director) {
    return employee.workDirectorTasks();
  } else {
    return employee.workTeacherTasks();
  }
}

type Subjects = "Math" | "History";

/**
 * tells current class
 *
 * @param todayClass today's subject
 * @returns string says which class to be taught today
 */
function teachClass(todayClass: Subjects): string {
  return `Teaching ${todayClass}`;
}

// console.log(createEmployee(200));
// console.log(createEmployee(1500));
// console.log(executeWork(createEmployee(50)));
// console.log(executeWork(createEmployee(1500)));
console.log(teachClass("Math"));
console.log(teachClass("History"));
