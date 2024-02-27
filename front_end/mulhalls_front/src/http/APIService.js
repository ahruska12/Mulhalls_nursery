import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';
const token = localStorage.getItem('token');
//verify token on every request except register/authenticate login/ find customer account

//axios.get('/api/data', {headers: {'Authorization': `Bearer ${token}`}}).then(response => {}).catch(error => {});

export class APIService {
    constructor() {

    }
    //posts user credentials to db, hashes pw on frontend
    registerUser(credentials) {
        const url = `${API_URL}/user/register/customer`;
        return axios.post(url, credentials);
    }
    //user login, this sends user credentials to backend to get auth token and isAuthenticated flag
    //this is called after user signs in
    authenticateLogin(credentials) {
        const username = credentials.username
        console.log(credentials);
        const url = `${API_URL}/user/auth/${username}`;
        return axios.post(url);
    }
    //same as registering user but for employees, once employee admin status and permissions work this will allow
    //employees who are admins to make new employees
    //sends employee creds to backend db
    registerEmployee(credentials) {
        const url = `${API_URL}/user/register/employee`;
        return axios.post(url, credentials);
    }
    //this gets customer account from db when given username, used for password verification
    findCustomerAccount(email) {
        const url = `${API_URL}/user/find-account/customer/${email}`;
        return axios.get(url);
    }
}

export class APIGetPlants {
    constructor() {

    }
    //returns list of plants to display in main menu
    getPlantList() {
        const url = `${API_URL}/product/home`;
        return axios.get(url);
    }
    //returns list of plants depending on the category
    getPlantsByCategory(category_type) {

    }
    //returns plants by department
    getPlantByDepartment(department_id) {

    }
    //returns specific plants
    getPlantByID(plant_id) {

    }
    //returns most popular searches
    getMostPopularSearches() {

    }
    //returns list of plants recently searched by specific user
    getRecentSearchesByUser(user_id) {

    }
}

export class APIQuestions {
    constructor() {
    }
    //posts question to db
    askQuestion(question) {

    }
    //returns questions asked by specific user
    findQuestionByUser(username) {

    }
    //returns questions asked about a specific plant
    findQuestionByPlant(plant_id) {

    }
    //returns questions asked on a specific date
    findQuestionByDate(date) {

    }
    //posts answer to question in db
    answerQuestion(question_id) {

    }

}