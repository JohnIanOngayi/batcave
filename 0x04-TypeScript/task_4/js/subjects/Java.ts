#!/usr/bin/node

/// <reference path='./Teacher.ts' />
/// <reference path='./Subject.ts' />

namespace Subjects {
  export interface Teacher {
    experienceTeachingJava?: number;
  }

  export class Java extends Subjects.Subject {
    getRequirements(): string {
      return "Here is the list of requirements for Java";
    }
    getAvailableTeacher(teacher: Subjects.Teacher): string {
      if (teacher.experienceTeachingJava) {
        return `Available Teacher: ${teacher.firstName}`;
      } else {
        return "No available teacher";
      }
    }
  }

  const java: Subjects.Java = new Subjects.Java();
}
