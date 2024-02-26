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
        console.log(credentials)
        const url = `${API_URL}/user/auth/`;
        return axios.post(url, credentials);
    }
    registerEmployee(credentials) {
        const url = `${API_URL}/user/register/employee`;
        return axios.post(url, credentials);
    }
    findCustomerAccount(email) {
    const url = `${API_URL}/user/find-account/customer/${encodeURIComponent(email)}`;
    return axios.get(url)
        .then(response => {
            // Handle successful response
            console.log(response.data, "this is the response")
            return response.data;// Assuming the response contains the password
        })
        .catch(error => {
            // Handle error
            console.error('Error finding customer account:', error);
            throw error; // You might want to handle the error differently
        });
}


}