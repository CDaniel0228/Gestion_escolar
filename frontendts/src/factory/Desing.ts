import { Materia } from "../models/Materia";
import { Salon } from "../models/Salon";
import { StudentModel } from "../models/StudentModel";

class Desing {
    createEstudiante(id: number, name: string, age: number, gender:string): StudentModel {
      return new StudentModel(id, name, age, gender);
    }
  
    createSalon(nombre: string): Salon {
      return new Salon(nombre,2);
    }
  
    createMateria(nombre: string): Materia {
      return new Materia(nombre, 2);
    }
  }
  
  export default Desing;
  