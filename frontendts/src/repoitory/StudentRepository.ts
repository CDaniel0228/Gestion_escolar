import { StudentModel } from "../models/StudentModel";
import ApiService from "../services/ApiServices";

export  class StudentRepository {
 
  static registerStudent(estudiante: StudentModel): Promise<any> {
    return ApiService.post('prueba/default/register', estudiante);
  }
      
}