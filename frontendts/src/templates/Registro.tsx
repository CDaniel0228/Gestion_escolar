// src/components/Registro.tsx
import React, { useState } from 'react';
import './Registro.css'; // Archivo CSS para los estilos
import Navbar from './Nav'
import { StudentModel } from '../models/StudentModel';
import { StudentRepository } from '../repoitory/StudentRepository';


function Registro () {
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


  return (
    <>
    <Navbar />
    <div className="registro-container">
      <h2>Registro de Estudiantes</h2>
      <form onSubmit={handleSubmit} className="registro-form">
      <label>
          Identificacion:
          <input type="text" name="id"  value={estudiante.id} onChange={handleChange} />
        </label>
        <label>
          Nombre:
          <input type="text" name="name"  value={estudiante.name} onChange={handleChange} />
        </label>
        <label>
          Edad:
          <input type="text" name="age" value={estudiante.age} onChange={handleChange} />
        </label>
        <label>
          Genero:
          <input type="text"  pattern="[F|M]" name="gender" value={estudiante.gender} onChange={handleChange} />
        </label>  
        <br />
        
        <button type="submit">Registrar</button>
      </form>
    </div>

    </>
  );
};

export default Registro;
