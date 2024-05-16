<template>
  <div class="home-container">
    <h1 class="home-title">Welcome to the Mulhall's Plant Support System</h1>
    <div class="image-container">
      <img src="../assets/mulhalls_background.jpg" alt="Mulhall's Background" class="home-image">
    </div>
    <h2 class="section-title">Here are some of our popular plants!</h2>
    <div class="home-plant-list">
      <div v-for="plant in popularPlantList" :key="plant.plant_id">
      <div class="card-body" @click="getPlantDetail(plant.plant_id)" style="cursor: pointer;">
        <h5 class="card-title">{{ plant.plant_name }}</h5>
        <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name" class="plant-image" style="cursor: pointer;">
      </div>
      </div>
    </div>
    <div v-if="isLoggedIn || isEmpl">
    <h2 class="section-title">Here are your recent searches!</h2>
    <div class="home-plant-list">
      <div v-for="plant in userRecentPlants" :key="plant.plant_id">
      <div class="card-body" @click="getPlantDetail(plant.plant_id)" style="cursor: pointer;">
        <h5 class="card-title">{{ plant.plant_name }}</h5>
        <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name" class="plant-image" style="cursor: pointer;">
      </div>
      </div>
    </div>
    </div>
      <h2 class="section-title">Here are some of our new plants!</h2>
      <div class="home-plant-list">
        <div class="home-plant-list">
      <div v-for="plant in newPlants" :key="plant.plant_id">
      <div class="card-body" @click="getPlantDetail(plant.plant_id)" style="cursor: pointer;">
        <h5 class="card-title">{{ plant.plant_name }}</h5>
        <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name" class="plant-image" style="cursor: pointer;">
      </div>
      </div>
    </div>
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
      popularPlantList: {},
      userRecentPlants: {},
      newPlants: {},
      user_id: "",
      search_info: {"plant": "",
                    "customer": "0"},
    };
  },
  methods: {
    ...mapActions([
      'checkAuth',
    ]),
    // Fetch list of all plants
    async fetchPlants() {
      try {
        const response = await plantAPI.getMostPopularSearches();
        this.popularPlantList = response.data;
        const recentResponse = await plantAPI.getRecentPlants();
        this.newPlants = recentResponse.data;
        if (this.isEmpl) {
          this.user_id = this.account_info.employee_id;
        }
        if (this.isLoggedIn && !this.isEmpl) {

          this.user_id = this.account_info.customer_id;
        }
        if (this.isLoggedIn) {
          const userResponse = await plantAPI.getRecentSearchesByUser(this.user_id);
          this.userRecentPlants = userResponse.data;
        }
      } catch (error) {
        console.error("Failed to fetch plants:", error);
      }
      console.log("Plant list:", this.popularPlantList);
      console.log("User list:", this.userRecentPlants);
      console.log("new list:", this.newPlants);
    },
    getImageUrl(relativePath) {
      return `http://mulhalls1nursery.pythonanywhere.com${relativePath}`;
    },
    getPlantDetail(plant_id) {
      console.log("search info: ", this.search_info)
      this.search_info.plant = plant_id;
      if (!this.isEmpl && this.isLoggedIn) {
        this.search_info.customer = this.account_info.customer_id;
      }
      if (this.isEmpl) {
        this.search_info.customer = this.account_info.employee_id;
      }
      plantAPI.addPlantSearch(this.search_info)
      console.log("search info: ", this.search_info)
      router.push(`plants/${plant_id}`);
    },
  },
  mounted() {
    this.checkAuth();
    this.fetchPlants();
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