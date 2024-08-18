/// <reference path='./Teacher.ts' />
// Define class Subject
namespace Subjects {
  export class Subject {
    teacher: Subjects.Teacher;
    set setTeacher(teacher: Subjects.Teacher) {
      this.teacher = teacher;
    }
  }
}
