<template>
  <div id="app">
    <nav>
      <ul class="nav-list">
        <li><button class="nav-button" @click="Home">Home</button></li>
        <li><button class="nav-button" @click="PlantList">Plants List</button></li>
        <li v-if="isEmpl"><button class="nav-button" @click="Questions">Questions</button></li>
        <li v-if="isEmpl"><button class="nav-button" @click="addPlant">Add Plants</button></li>
        <li><div class="username">Welcome {{ isLoggedIn ? username : 'Guest' }}!</div></li>
        <li v-if="isLoggedIn & !isEmpl"><button class="nav-button" @click="userQuestions">My Questions</button></li>
        <li v-if="!isLoggedIn"><button class="nav-button" @click="Register">Register</button></li>
        <li v-if="!isLoggedIn"><button class="nav-button" @click="Login">Login</button></li>
        <li v-if="isLoggedIn"><button class="nav-button" @click="Logout">Logout</button></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Navbar',
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      username: state => state.username,
    }),
  },
  methods: {
    ...mapActions([
      'logout',
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
    userQuestions() {
      this.$router.push('/current-questions')
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
      this.logout();
    },
  },
}
</script>

<style scoped>
/* Styles for the navigation bar */
nav {
  display: flex;
  justify-content: center; /* Center items horizontally */
}

.nav-list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

nav ul li {
  margin-right: 10px;
}

.nav-button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

.nav-button:hover {
  background-color: #45a049;
}

.username {
  margin-top: 5px;
  font-weight: bold;
}

</style>