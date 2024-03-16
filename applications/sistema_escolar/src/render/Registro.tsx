// src/components/Registro.tsx
import React from 'react';
import './Registro.css'; // Archivo CSS para los estilos
import { StudentFormController } from '../controller/StudentFormController';


function Registro () {
  const { estudiante, handleChange, handleSubmit } = StudentFormController();

  return (
    <>
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
