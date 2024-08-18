#!/usr/bin/node

/// <reference path='./Teacher.ts' />
/// <reference path='./Subject.ts' />

namespace Subjects {
  export interface Teacher {
    experienceTeachingReact?: number;
  }

  export class React extends Subjects.Subject {
    getRequirements(): string {
      return "Here is the list of requirements for React";
    }
    getAvailableTeacher(): string {
      if (this.teacher.experienceTeachingReact) {
        return `Available Teacher: ${this.teacher.firstName}`;
      } else {
        return "No available teacher";
      }
    }
  }

  export const react: Subjects.React = new React();
}
