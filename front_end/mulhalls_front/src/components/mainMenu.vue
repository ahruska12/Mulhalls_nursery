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
</template>

<script>
 import router from '../router';
 import {APIService} from '../http/APIService';
 const apiService = new APIService();


 export default {
   name: 'mainMenu',

   data: () => ({
     valid: true,
     showMsg: '',
     loading: false,
     username: "Guest"
   }),
   methods: {
     checkAuth() {
       //everytime the webpage is reloaded it checks to make sure the user is authenticated
       console.log("checkAuth called");
       try {
         if (localStorage.getItem("isAuthenticates") && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
           this.username = localStorage.getItem("log_user");
         } else {
           console.log("not authenticated");
         }
       } catch (error) {
         console.error("Error occurred during authentication check:", error);
       }
     },
   },
   created() {
       this.checkAuth();
   }
 }
</script>

<style scoped>

</style>