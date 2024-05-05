<template>
  <div class="home-container">
    <h1 class="home-title">Welcome to the Mulhall's Plant Support System</h1>
    <div class="image-container">
      <!-- Insert your image here -->
      <img src="../assets/mulhalls_background.jpg" alt="Mulhall's Background" class="home-image">
    </div>
    <div class="section">
      <h2 class="section-title">Here are some of our popular plants this month!</h2>
      <!-- Add content for popular plants -->
    </div>
    <div class="section">
      <h2 class="section-title">Here are some of our new plants!</h2>
      <!-- Add content for new plants -->
    </div>
  </div>
</template>

<script>
import router from '../router';
import { APIGetPlants } from '../http/APIService';
import { mapState, mapActions } from 'vuex';

const plantAPI = new APIGetPlants();

export default {
  name: 'Home',
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      username: state => state.username,
      loading: state => state.loading,
      account_info: state => state.account_info,
    }),
  },
  data() {
    return {
      plantList: [],
    };
  },
  methods: {
    ...mapActions([
      'checkAuth',
    ]),
    // Fetch list of all plants
    async fetchPlants() {
      try {
        const response = await plantAPI.getPlantList();
        this.plantList = response.data;
        console.log("Plant list:", this.plantList);
      } catch (error) {
        console.error("Failed to fetch plants:", error);
      }
    },
  },
  mounted() {
    this.fetchPlants();
    this.checkAuth();
  },
};
</script>

<style>
.home-container {
  padding: 20px;
  text-align: center;
}

.home-title {
  font-size: 36px;
  margin-bottom: 20px;
  color: #333; /* Text color */
}

.image-container {
  margin-bottom: 40px;
}

.home-image {
  width: 100%;
  max-width: 800px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.section {
  margin-bottom: 40px;
}

.section-title {
  font-size: 24px;
  margin-bottom: 10px;
  color: #333; /* Text color */
  font-family: 'Montserrat', sans-serif; /* Modern font */

}

#app {
  background-color: rgb(204, 255, 204);
}
</style>