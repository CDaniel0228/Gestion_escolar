import { StudentModel } from "../models/StudentModel";

export class StudentFormRenderer {
  render(studentModel: StudentModel): string {
    return `
      <form id="student-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="${studentModel.name}" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Register</button>
      </form>
    `;
  }
}