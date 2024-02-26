import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';


export class APIService {
    constructor() {

    }
    registerUser(credentials) {
        const url = `${API_URL}/user/register/customer`;
        return axios.post(url, credentials);
    }
    authenticateLogin(credentials) {
        const password = credentials.password
        console.log(credentials);
        const url = `${API_URL}/user/auth/${password}`;
        return axios.post(url, password);
    }
    registerEmployee(credentials) {
        const url = `${API_URL}/user/register/employee`;
        return axios.post(url, credentials);
    }
    findCustomerAccount(email) {
        const url = `${API_URL}/user/find-account/customer/${email}`;
        return axios.get(url);
}


}