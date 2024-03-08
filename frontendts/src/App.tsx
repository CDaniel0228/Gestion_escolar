import React from 'react';    
import {BrowserRouter, Routes, Route } from "react-router-dom"
import Formulario from "./templates/Formulario"
import Tareas from './templates/Tareas';
import Registro from './templates/Registro';
import Nav from './templates/Nav';
import Error404 from './templates/Error404';
import StudentForm from './templates/StudentForm';
import { StudentModel } from './models/StudentModel';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ <Registro/> } />
        <Route path="/asistencia" element={ <Tareas /> } />
        <Route path="/EstudentForm" element={ <StudentForm onStudentRegistered={function (student: StudentModel): void {
          throw new Error('Function not implemented.');
        } } /> } />
        <Route path="*" element={<Error404 />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App