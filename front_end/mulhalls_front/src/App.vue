<template>
  <div id="app">
    <nav>
      <ul>
        <li><button @click="Home">Home</button></li>
        <li><button @click="PlantList">Plants List</button></li>
        <li><button v-if="isEmpl" @click="Questions">Questions</button></li>
        <li><div v-if="isLoggedIn" class="username">Welcome {{username}}!</div></li>
        <li><div v-if="!isLoggedIn" class="username">Welcome Guest!</div></li>
        <li><button v-if="!isLoggedIn" @click="Register">Register</button></li>
        <li><button v-if="!isLoggedIn" @click="Login">Login</button></li>
        <li><button v-if="isLoggedIn" @click="Logout">Logout</button></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

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
  methods: {
    ...mapActions([
      'logout', // Action to log out
      'checkAuth', // Action to check authentication
      // Add other actions you need to dispatch
    ]),
    Home() {
      this.$router.push('/');
    },
    PlantList() {
      this.$router.push('/plants');
    },
    Questions() {
      this.$router.push('/questions');
    },
    Register() {
      this.$router.push('/registerUser');
    },
    Login() {
      this.$router.push('/authUser');
    },
    Logout() {
      this.logout(); // Dispatch the logout action instead of changing data directly
    },
  },
  created() {
    //doesn't want to work most of the time, might just add this to every page to ensure it works every time a page is loaded
    //muted for now.....
    //this.checkAuth();
  }
}
</script>

<style scoped>
/* Styles for the navigation bar */

body, html {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  height: 100%;
  width: 100%;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

nav {
  display: flex;
  width: 100vh;
  justify-content: space-between; /* Space out menu bar items */
  align-items: center; /* Center items vertically */
  background-color: rgb(31,47,39); /* Menu bar background color */
  padding: 10px; /* Padding around the menu bar */
  box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* Shadow for some depth */
}

nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav ul li {

}

nav ul li button {
  color: rgb(31,47,39);
  text-decoration: none;
  padding: 8px 16px; /* You can adjust this as needed */
  border-radius: 8px;
  background-color: white; /* Removes the button styling */
}

nav ul li button:hover {
  background-color: rgb(31,47,39);
  color: white;
}

.username {
  padding: 8px 16px; /* Adjust username padding to match buttons */
  color: white;
}
</style>