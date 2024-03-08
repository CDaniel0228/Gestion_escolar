import { StudentModel } from "../models/StudentModel";
import { StudentRepository } from "../repoitory/StudentRepository";

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export class StudentFormController {
  private studentModel: StudentModel;
  private form: HTMLFormElement;
  private studentRepository: StudentRepository;

  constructor(studentModel: StudentModel, form: HTMLFormElement) {
    this.studentModel = studentModel;
    this.form = form;
    this.studentRepository = new StudentRepository();

    this.form.addEventListener('submit', this.handleSubmit.bind(this));
  }

  private async handleSubmit(event: Event): Promise<void> {
    event.preventDefault();

    const name = this.form.querySelector('#name') as HTMLInputElement;
    const email = this.form.querySelector('#email') as HTMLInputElement;
    //const age = this.form.querySelector('#age') as HTMLInputElement;
    //const course = this.form.querySelector('#course') as HTMLInputElement;

    this.studentModel.name = name.value;
    this.studentModel.age = 0;
    //this.studentModel.age = parseInt(age.value, 10);
    //this.studentModel.course = course.value;

    /*try {
      await this.studentRepository.registerStudent(this.studentModel);
      alert('Student registered successfully');
    } catch (error) {
      alert('Error registering student');
    }*/
  }
}