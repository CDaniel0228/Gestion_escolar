import { StudentFormController } from "../controller/StudentFormController";
import { StudentModel } from "../models/StudentModel";
import { StudentFormRenderer } from "../render/FormRenderer";

export class StudentFormFactory {
  create(studentModel: StudentModel): StudentFormController {
    const formRenderer = new StudentFormRenderer();
    const formHtml = formRenderer.render(studentModel);

    const formElement = document.createElement('div');
    formElement.innerHTML = formHtml;

    const form = formElement.querySelector('#student-form') as HTMLFormElement;

    return new StudentFormController(studentModel, form);
  }
}

