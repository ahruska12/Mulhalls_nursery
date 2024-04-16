<template>
  <div class="menu-bar">
    <div class="dropdown">
      <button class="categories-btn" @click="toggleDropdown">Category: {{category}}</button>
      <div class="dropdown-content" v-if="showDropdown">
        <a v-for="category in categories" :key="category" @click="selectCategory(category)">
          {{ category }}
        </a>
      </div>
    </div>
    <input type="text" placeholder="Search" class="search-box">
    <button v-if="isEmpl" class="question-btn">Questions</button>
    <button v-if="!isLoggedIn" @click="login" class="login-btn">Login</button>
    <div v-if="isLoggedIn" class="username">{{this.username}}</div>
    <button v-if="isLoggedIn" @click="logout" class="logout-btn">Logout</button>
    <div v-if="!isLoggedIn" class="username">Guest</div>
  </div>
  <div class="main-container">
      <h1>{{category}}</h1>
      <div v-for="plant in plant_list" v-bind:key="plant.plant_id" class="card">
        <h1>{{plant.plant_name}}</h1>
      </div>
  </div>
</template>

<script>
 import router from '../router';
 import {APIGetPlants, APIService} from '../http/APIService';
 import {toRaw} from "vue";

 const plantAPI = new APIGetPlants();
 const apiService = new APIService();


 export default {
   name: 'mainMenu',

   data: () => ({
     valid: true,
     showMsg: '',
     loading: false,
     username: "Guest",
     isEmpl: false,
     plant_list: [],
     isLoggedIn: false,
     showDropdown: false,
     categories: ['All Plants','Annual', 'Perennial', 'Tree', 'Shrub'],
     category: "All Plants",
   }),
   methods: {
     //login method
     login() {
      // will perform login function here
       router.push()
       this.isLoggedIn = true;
       console.log('User logged in:', this.username);
    },
     //logout method
     logout() {
       // will perform a logout here
       this.isLoggedIn = false;
       console.log('User logged out');
     },
     //this shows the dropdown
     toggleDropdown() {
       this.showDropdown = !this.showDropdown;
     },
     //this picks the category dropdown
     selectCategory(category) {
       this.category = category;
       console.log('Category selected:', category);
       // Perform actions when a category is selected
       this.showDropdown = false;
     },
     //I don't think this method is needed will hold here for now
     getAcc() {
       apiService.findCustomerAccount(this.username).then(response => {
              this.account_info = response.data;
            })
           .catch(error => {
             console.error(error);
           });
     },
     checkAuth() {
       //everytime the webpage is reloaded it checks to make sure the user is authenticated
       console.log("checkAuth called");
       try {
         if (localStorage.getItem("isAuthenticated") && JSON.parse(localStorage.getItem("isAuthenticated")) === true) {
           this.username = localStorage.getItem("log_user");
           this.isLoggedIn = true;
         } else {
           console.log("not authenticated");
         }
         if (localStorage.getItem("isAdmin") === "1") {
           this.isEmpl = true;
           console.log(this.isEmpl, "emp check")
         }
       } catch (error) {
         console.error("Error occurred during authentication check:", error);
       }
     },
     getPlantList() {
       plantAPI.getPlantList().then((response) => {
         this.plant_list = response.data;
         console.log("plant list", this.plant_list);
       }).catch(e => {
         console.error(e);
       });
     }
   },
   mounted() {
     this.getPlantList();
   },
   created() {
       this.checkAuth();
   }
 }
</script>

<style>

html, body, header, * {
  margin: 0;
  padding: 0;
  box-sizing: border-box; /* Include padding and border in the width and height */
}

/* Styles for the menu bar */
.menu-bar {
  display: flex;
  width: 100vh;
  justify-content: space-between; /* Space out menu bar items */
  align-items: center; /* Center items vertically */
  background-color: #f8f8f8; /* Menu bar background color */
  padding: 10px; /* Padding around the menu bar */
  box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Shadow for some depth */
}

.menu-bar button {
  padding: 8px 15px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.menu-bar button:hover {
  background-color: #0056b3;
}

.main-container {
}

.card {
  border: 1px solid black;
  border-radius: 8px;
  margin: 20px;
  color: whitesmoke;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #333333;
  padding: 10px;
}

.username {
  color: #181818;
}

.search-box {
  padding: 8px;
  border: 2px solid #ccc;
  border-radius: 5px;
}

.search-box:focus {
  border-color: #007BFF;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>