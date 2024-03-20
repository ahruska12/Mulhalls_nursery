<template>
  <div v-if="username === 'Guest'">
    <div class="welcome-screen">
      <h1>Sign in for more features!</h1>
      <p>Login</p>
      <p>Register</p>
    </div>
  </div>
  <div v-if="username !== 'Guest'">
    <div class="welcome-screen">
      <h1>Welcome {{username}}!</h1>
    </div>
  </div>
  <div class="main-container">
    <div class="card">
      <div v-for="plant in plant_list" v-bind:key="plant_id">
        <h1>{{plant.color}} {{plant.description}}</h1>
      </div>
    </div>
  </div>
</template>

<script>
 import router from '../router';
 import {APIGetPlants, APIService} from '../http/APIService';
 const plantAPI = new APIGetPlants();
 const apiService = new APIService();


 export default {
   name: 'mainMenu',

   data: () => ({
     valid: true,
     showMsg: '',
     loading: false,
     username: "Guest",
     plant_list: "",
   }),
   methods: {
     getAcc() {
       apiService.findCustomerAccount(this.username).then(response => {
              this.stored_info = response.data;
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
         } else {
           console.log("not authenticated");
         }
       } catch (error) {
         console.error("Error occurred during authentication check:", error);
       }
     },
     getPlantList() {
       const token = localStorage.getItem("token");
       if (!token) {
         console.error("JWT token is missing");
         return; // Exit the function if there's no token
       }
       plantAPI.getPlantList(token).then((response) => {
         this.plant_list = response.data;
         console.log("plantttttt", this.plant_list[1]);
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

<style scoped>

</style>