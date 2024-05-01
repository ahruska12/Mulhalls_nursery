import axios from 'axios';
const API_URL ='http://127.0.0.1:8000';

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
    authenticateEmpLogin(credentials) {
        const username = credentials.username
        //make sure to take this out at some point....
        console.log(credentials);
        const url = `${API_URL}/user/auth/employee/${username}`;
        return axios.post(url);
    }
    //this gets customer account from db when given username, used for password verification
    findCustomerAccount(email) {
        const url = `${API_URL}/user/find-account/customer/${email}`;
        return axios.get(url);
    }
    //this gets employee account from db to authenticate employee acct on sign in, right now it doesn't work!
    findEmployeeAccount(email) {
        const url = `${API_URL}/user/find-account/employee/${email}`;
        return axios.get(url);
    }

    getDepartments() {
        const url = `${API_URL}/user/departments`;
        return axios.get(url)
    }
}

export class APIGetPlants {
    constructor() {

    }
    addPlant(plant_info) {
        const url = `${API_URL}/product/add/plant`;
        return axios.post(url, plant_info, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
        console.log('Plant added with ID:', response.data.plant_id);
        return response.data;
        }).catch(error => {
            console.error('Error adding plant:', error.response.data);
            throw error;
        });
    }

    addAnnual(plant_info) {
        const url = `${API_URL}/product/add/plant-annual`;
        return axios.post(url, plant_info);
    }
    //returns list of plants to display in main menu
    getPlantList() {
        const url = `${API_URL}/product/home/`;
        return axios.get(url);
    }
    getPlantPrevByID(plant_id) {
        const url = `${API_URL}/product/plant/prev/${plant_id}`;
        return axios.get(url);
    }
    //returns list of plants depending on the category - done
    getPlantsByCategory(category_type) {
        const url = `${API_URL}/product/plant/type/${category_type}`;
        return axios.get(url);
    }
    //returns plants by department - done
    getPlantByDepartment(department_id) {
        const url = `${API_URL}/product/plant/dept${department_id}`;
        return axios.get(url);
    }
    //returns plants by color - done
    getPlantByColor(plant_color) {
        const url = `${API_URL}/product/plant/color/${plant_color}`;
        return axios.get(url);
    }
    //returns plant by specific category - done
    getPlantBySpecialCategory(plant_type, category) {
        const url = `${API_URL}/product/plant/category/${plant_type}/${category}`;
        return axios.get(url);
    }
    //returns specific plants - done
    getPlantByID(plant_id) {
        const url = `${API_URL}/product/plant/select/${plant_id}`;
        return axios.get(url);
    }
    //gets list of plants from list of plant ids
    getPlantByArr(arr) {
        const url = `${API_URL}/product/plant/group?ids=${arr.join(',')}`;
        return axios.get(url);
    }
    //returns most popular searches
    getMostPopularSearches() {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
    //returns list of plants recently searched by specific user
    getRecentSearchesByUser(user_id) {
        const url = `${API_URL}/product`;
        return axios.get(url);
    }
}
//commented out methods aren't needed (right now)
export class APIQuestions {
    constructor() {
    }
    //posts question to db requires cust_id, plant_id, and question in that order - done
    askQuestion(question_details) {
        const url = `${API_URL}/user/ask/question`;
        return axios.post(url, question_details);
    }
    //returns all questions - done
    listQuestions() {
        const url = `${API_URL}/user/list/questions`;
        return axios.get(url);
    }
    //returns all unanswered questions - done
    listUnQuestions(v) {
        const url = `${API_URL}/user/list/questions/${v}`;
        return axios.get(url);
    }
    //returns questions asked by specific customer - done
    //findQuestionByUser(cust_id) {
    //    const url = `${API_URL}/user/find/questions-cust/${cust_id}`;
    //    return axios.get(url);
    //}
    //returns answered questions asked about a specific plant - done
    findQuestionByPlant(plant_id) {
       const url = `${API_URL}/user/find/questions-plant/${plant_id}`;
       return axios.get(url);
    }

     //returns questions asked by question id - done
    findQuestionByID(question_id) {
        const url = `${API_URL}/user/find/questions-id/${question_id}`;
        return axios.get(url);
    }

    //posts answer to question in db, arr is either going to be array of question id, emp number, answer, and date, or
    //seperate variables
    // answer should contain in this exact order - question_id, employee_id, answer - done
    answerQuestion(answer) {
        const url = `${API_URL}/user/answer/question`;
        return axios.post(url, answer);
    }

}