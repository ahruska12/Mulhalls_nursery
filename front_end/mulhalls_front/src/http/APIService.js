import axios from 'axios';
const API_URL ='';


export class APIService {
    constructor() {

    }
    registerUser(credentials) {
     const url = `${API_URL}/register/`;
     credentials.customusername = credentials.username
     return axios.post(url, credentials);
  }
}