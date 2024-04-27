<template>
  <h1>Welcome to the Mulhall's Plant Support System</h1>
  <br>
  <h1>Here are some of our popular plants this month!</h1>
  <br>
  <h1>Here are some of our new plants!</h1>
</template>

<script>
 import router from '../router';
 import {APIGetPlants, APIService} from '../http/APIService';
 import {toRaw} from "vue";
 import { mapState, mapActions } from 'vuex';

 const plantAPI = new APIGetPlants();
 const apiService = new APIService();


 export default {
   name: 'Home',
   computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      email: state => state.email,
      username: state => state.username,
      loading: state => state.loading,
      account_info: state => state.account_info,
    }),
  },
   data: () => ({
     valid: true,
     //message variable
     showMsg: '',
     //list of all plants for main dashboard
     plant_list: [],
   }),
   methods: {
     ...mapActions([
      'logout', // Action to log out
      'checkAuth', // Action to check authentication
      // Add other actions you need to dispatch
    ]),
     //list of all plants
     getPlantList() {
       plantAPI.getPlantList().then((response) => {
         this.plant_list = response.data;
         console.log("plant list", this.plant_list);
       }).catch(e => {
         console.error(e);
       });
     }
   },
   //these are loaded on refresh
   mounted() {
     this.getPlantList();
     this.checkAuth();
   },
   //these should be loaded on refresh of page
   created() {

   }
 }
</script>

<style>
</style>