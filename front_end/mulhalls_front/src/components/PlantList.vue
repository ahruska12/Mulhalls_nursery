<template>
  <div class="plant-list-search">
    <!-- Search and Filter Section -->
    <input v-model="searchQuery" @input="filterPlants" type="text" placeholder="Search plants...">
    <select v-model="selectedType" @change="filterPlants" class="form-control">
      <option value="">All Types</option>
      <option v-for="type in types" :key="type" :value="type">{{ type }}</option>
    </select>
  </div>
  <div class="main-container-plant-list">
    <div v-if="filteredPlants.length === 0">No plants found.</div>
    <div v-for="plant in sortedFilteredPlants" :key="plant.plant_id">
      <div class="card-body" @click="getPlantDetail(plant.plant_id)" style="cursor: pointer;">
        <h5 class="card-title">{{ plant.plant_name }}</h5>
        <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name" class="plant-image" style="cursor: pointer;">
      </div>
    </div>
  </div>
</template>

<script>
import { APIGetPlants } from '@/http/APIService';
import router from "@/router/index.js";
import {mapActions, mapState} from "vuex";
const plantApi = new APIGetPlants()

export default {
  name: 'PlantList',
  data() {
    return {
      plant: [],
      filteredPlants: [],
      searchQuery: '',
      selectedType: '',
      sortKey: 'name',
      types: ['Shrub', 'Tree', 'Annual', 'Perennial'],
      search_info: {"plant": "",
                    "customer": "0"},
      isLoading: false
    };
  },
  created() {
    this.fetchPlants();
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      email: state => state.email,
      username: state => state.username,
      loading: state => state.loading,
      account_info: state => state.account_info,
    }),
    sortedFilteredPlants() {
      if (this.sortKey === 'type') {
        return this.filteredPlants.slice().sort((a, b) => {
          return a.type.localeCompare(b.type);
        });
      } else {
        return this.filteredPlants;
      }
    }
  },
  methods: {
    ...mapActions([
      'logout', // Action to log out
      'checkAuth', // Action to check authentication
      // Add other actions you need to dispatch
    ]),
    fetchPlants() {
      this.isLoading = true;
      const apiService = new APIGetPlants();
      apiService.getPlantList()
        .then(response => {
          console.log("API Response:", response.data); // Log the response data
          this.plant = response.data;
          this.filteredPlants = this.plant;
          console.log("Filtered plants: ", this.filteredPlants);
        })
        .catch(error => {
          console.error("Failed to fetch plants:", error);
          // Show error message to the user
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    filterPlants() {
      this.filteredPlants = this.plant.filter((plant) => {
        const matchesSearchQuery = plant.plant_name.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesType = !this.selectedType || plant.plant_type === this.selectedType;
        return matchesSearchQuery && matchesType;
      });
    },
    getPlantDetail(plant_id) {
      this.search_info.plant = plant_id;
      if (!this.isEmpl && this.isLoggedIn) {
        this.search_info.customer = this.account_info.customer_id;
      }
      if (this.isEmpl) {
        this.search_info.customer = this.account_info.employee_id;
      }
      plantApi.addPlantSearch(this.search_info)
      router.push(`plants/${plant_id}`);
    },
    getImageUrl(relativePath) {
      return `http://127.0.0.1:8000${relativePath}`;
    }
  },
  mounted() {
    this.checkAuth();
  }
}
</script>

<style>
.plant-list-search {
  margin-top: 50px; /* Add margin to the top */
}

.plant-image {
  width: 200px;
  height: 200px;
  object-fit: cover; /* Maintain aspect ratio and crop if necessary */
}
.plant-image:hover {
  transform: scale(1.1); /* Increase size on hover */
}

.card-title {
  font-size: 1.2em; /* Increase font size */
  font-weight: bold; /* Increase font weight */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Add text shadow for better contrast */
}

.card-title:hover {
  color: blue; /* Change text color on hover */
}
</style>