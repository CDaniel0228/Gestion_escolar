import React, { useState } from "react";
import { StudentRepository } from "../repoitory/StudentRepository";
import { StudentModel } from "../models/StudentModel";
interface StudentFormProps {
  onStudentRegistered: (student: StudentModel) => void;
}

const StudentForm: React.FC<StudentFormProps> = ({ onStudentRegistered }) => {
  const [formData, setFormData] = useState<StudentModel>({
    id: 0,
    name: "",
    age: 0,
    gender:''
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e: React.ChangeEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await StudentRepository.registerStudent(formData);
      console.log(response)
      //onStudentRegistered(response);
    } catch (error) {
      console.error("Error registering student:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        First Name:
        <input
          type="text"
          name="id"
          value={formData.id}
          onChange={handleChange}
        />
      </label>
      <label>
        Last Name:
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
      </label>
      <label>
        Email:
        <input
          type="text"
          name="email"
          value={formData.age}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Register</button>
    </form>
  );
};

export default StudentForm;