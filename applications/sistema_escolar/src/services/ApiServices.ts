import { StudentModel } from "../models/StudentModel";

export default  class ApiService {
  static baseURL = 'http://127.0.0.1:8000/';
  static post(url: string, data: StudentModel): Promise<StudentModel> {
    return fetch(`${this.baseURL}${url}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .catch(error => {
      console.error('Error en la solicitud fetch:', error);
      throw error; // Esto permite que el error se propague y sea capturado en el lugar adecuado
    });
  }
}
