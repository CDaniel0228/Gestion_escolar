import { StudentModel } from "../models/StudentModel";
import { StudentRepository } from "../repository/StudentRepository";
import { useState } from 'react';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
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
    alert(`Respuesta del servidor: ${JSON.stringify(response)}`)
    setEstudiante({
      id: 0,
      name: '',
      age: 0,
      gender:''
    });
    
    console.log("d");
  };

  return { estudiante, handleChange, handleSubmit };
}


