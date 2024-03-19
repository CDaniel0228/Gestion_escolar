import { StudentModel } from "../models/StudentModel";
import { StudentRepository } from "../repository/StudentRepository";
import { useState } from 'react';

// Responsible for executing the actions of the student form
export function StudentFormController() {
  const [estudiante, setEstudiante] = useState<StudentModel>({
    id: 0,
    name: '',
    age: 0,
    gender:''
  });

  const handleChange = (event: { target: { name: any; value: any; }; }) => {
    const { name, value } = event.target;
    setEstudiante((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = async (event: { preventDefault: () => void; }) => {
    event.preventDefault();
    const response = await StudentRepository.registerStudent(estudiante);
    alert(`Server response: ${JSON.stringify(response.message)}`)
    setEstudiante({
      id: 0,
      name: '',
      age: 0,
      gender:''
    });    
  };

  return { estudiante, handleChange, handleSubmit };
}


