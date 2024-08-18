#!/usr/bin/node

// Define the Teacher interface with required and optional properties
interface Teacher {
  readonly firstName: string;
  readonly lastName: string;
  location: string;
  yearsOfExperience?: number;
  [key: string]: unknown;
}

// Define the Directors interface that extends Teacher and adds a new property
interface Directors extends Teacher {
  numberOfReports: number;
}

// Define the TeacherFunction interface that logs the Teacher object to the console
interface TeacherFunction {
  (firstName: string, lastName: string): string;
}

// interface for functions for StudentClass
interface StudentClassFn {
  (): string;
}

// interface for StudentClass constructor
interface StudentClassConstructor {
  new (firstName: string, lastName: string): StudentClassInterface;
}

// Define interface for class StudentClass
interface StudentClassInterface {
  firstName: string;
  lastName: string;
  workOnHomework: StudentClassFn;
  displayName: StudentClassFn;
}

class StudentClass implements StudentClassInterface {
  firstName: string;
  lastName: string;

  constructor(firstName: string, lastName: string) {
    this.lastName = lastName;
    this.firstName = firstName;
  }

  workOnHomework: StudentClassFn = () => {
    return "Currently working";
  };

  displayName: StudentClassFn = () => {
    return this.firstName;
  };
}

/**
 * function prints shortened name of teacher
 *
 * @param {string} firstName  first name of Teacher
 * @param {string} lastName  last name of Teacher
 * @returns {string}  1st character from first name and last name
 */
const printTeacherFunction: TeacherFunction = (
  firstName: string,
  lastName: string,
): string => {
  return `${firstName.charAt(0)}, ${lastName}`;
};

// Create a Teacher object with required and additional properties
const teacher3: Teacher = {
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
const director1: Directors = {
  firstName: "John",
  lastName: "Doe",
  location: "London",
  fullTimeEmployee: true,
  numberOfReports: 17,
};

const student1: StudentClass = new StudentClass("Charlie", "Brown");

// Log the Directors object to the console
// console.log(director1);
console.log("Student1: ", student1);
console.log(student1.workOnHomework());
console.log(student1.displayName());
