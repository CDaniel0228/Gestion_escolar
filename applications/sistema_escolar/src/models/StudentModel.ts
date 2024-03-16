// eslint-disable-next-line @typescript-eslint/no-unused-vars
export class StudentModel {
    id: number;
    name: string;
    age: number;
    gender: string;
    constructor(id: number, name: string, age: number, gender: string) {
      this.id = id;
      this.name = name;
      this.age = age;
      this.gender = gender;
    }
}