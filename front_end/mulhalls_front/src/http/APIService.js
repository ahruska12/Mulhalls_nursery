import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';


export class APIService {
    constructor() {

    }
    registerUser(credentials) {
        const url = `${API_URL}/user/register/`;
        return axios.post(url, credentials);
    }
    authenticateLogin(credentials) {
        const url = `${API_URL}/user/auth/`;
        return axios.post(url, credentials);
  }
}