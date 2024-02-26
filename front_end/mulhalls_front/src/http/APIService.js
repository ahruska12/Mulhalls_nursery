import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';
const token = localStorage.getItem('token');
//verify token on every request except register/authenticate login/ find customer account

//axios.get('/api/data', {headers: {'Authorization': `Bearer ${token}`}}).then(response => {}).catch(error => {});

export class APIService {
    constructor() {

    }
    registerUser(credentials) {
        const url = `${API_URL}/user/register/customer`;
        return axios.post(url, credentials);
    }
    authenticateLogin(credentials) {
        const username = credentials.username
        console.log(credentials);
        const url = `${API_URL}/user/auth/${username}`;
        return axios.post(url);
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