<template>
  <div class="main-container">
      <div v-for="plant in plant_list" v-bind:key="plant.plant_id" class="card">
        <h1>{{plant.plant_name}}</h1>
      </div>
  </div>
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
     //dropdown menu shown or not
     showDropdown: false,
     //categories for each plant
     categories: ['All Plants','Annual', 'Perennial', 'Tree', 'Shrub'],
     //current category
     category: "All Plants",
   }),
   methods: {
     ...mapActions([
      'logout', // Action to log out
      'checkAuth', // Action to check authentication
      // Add other actions you need to dispatch
    ]),
     //this shows the dropdown
     toggleDropdown() {
       //toggle just does the opposite of what is currently being shown
       this.showDropdown = !this.showDropdown;
     },
     //this picks the category dropdown
     selectCategory(category) {
       //so we can display the current category
       this.category = category;
       console.log('Category selected:', category);
       // once category selected dropdown goes away
       this.showDropdown = false;
     },
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