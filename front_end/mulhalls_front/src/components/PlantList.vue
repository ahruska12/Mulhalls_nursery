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