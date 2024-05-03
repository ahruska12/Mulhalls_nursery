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
      <div class="card-body" @click="getPlantDetail(plant.plant_id)">
        <h5 class="card-title">{{ plant.plant_name }}</h5>
        <p class="card-text">{{ plant.plant_description }}</p>
        <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name">
      </div>
    </div>
  </div>
</template>

<script>
import { APIGetPlants } from '@/http/APIService';
import router from "@/router/index.js";

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
      isLoading: false
    };
  },
  created() {
    this.fetchPlants();
  },
  computed: {
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
      router.push(`plants/${plant_id}`);
    },
    getImageUrl(relativePath) {
      return `http://127.0.0.1:8000${relativePath}`;
    }
  }
}
</script>

<style>

</style>