/// <reference path='./Cpp.ts' />

// Define interface for Teacher obj
namespace Subjects {
  export interface Teacher {
    firstName: string;
    lastName: string;
  }

  export const cTeacher: Subjects.Teacher = {
    firstName: "John",
    lastName: "Doe",
    experienceTeachingC: 10,
  };
}
