<template>
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