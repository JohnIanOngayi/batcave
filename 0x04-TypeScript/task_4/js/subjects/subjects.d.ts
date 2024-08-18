declare module "namespace_Subjects" {
  export namespace Subjects {
    export class Cpp {
      getRequirements(): string;
      getAvailableTeacher(): string;
    }

    export const cpp: Cpp = new Cpp();

    export class Java {
      getRequirements(): string;
      getAvailableTeacher(): string;
    }

    export const java: Java = new Java();

    export class React {
      getRequirements(): string {}
      getAvailableTeacher(): string;
    }

    export const react: React = new React();

    export class Subject {
      teacher: Subjects.Teacher;
      set setTeacher(teacher: Subjects.Teacher): void;
    }

    export interface Teacher {
      firstName: string;
      lastName: string;
      experienceTeachingC?: number;
      experienceTeachingReact?: number;
      experienceTeachingJava?: number;
    }

    export const cTeacher: Teacher = new Teacher();
  }
}
