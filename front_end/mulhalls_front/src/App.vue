<template>
  <div id="app">
    <nav>
      <ul>
        <li><button @click="Home">Home</button></li>
        <li><button @click="PlantList">Plants List</button></li>
        <li><button v-if="isEmpl" @click="Questions">Questions</button></li>
        <li><button v-if="isEmpl" @click="addPlant">Add Plants</button></li>
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
    addPlant() {
      this.$router.push('/add/plant');
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

</style>