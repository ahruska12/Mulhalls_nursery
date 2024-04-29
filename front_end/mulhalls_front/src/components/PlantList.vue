<template>
  <div class="plant_list">
    <!-- Search and Filter Section -->
    <div class="filters row mb-3">
      <div class="col-md-4">
        <input v-model="searchQuery" @input="filterPlants" type="text" class="form-control" placeholder="Search plants...">
      </div>
      <div class="col-md-4">
        <select v-model="selectedType" @change="filterPlants" class="form-control">
          <option value="">All Types</option>
          <option v-for="type in types" :key="type" :value="type">{{ type }}</option>
        </select>
      </div>
    </div>

    <!-- Plants Display -->
    <div class="row">
      <div class="col-md-4" v-for="plant in filteredPlants" :key="plant.plant_id">
        <div class="card mb-4 shadow-sm">
          <div class="card-body" @click="getPlantDetail(plant.plant_id)">
            <h5 class="card-title">{{ plant.plant_name }}</h5>
            <p class="card-text">{{ plant.plant_description }}</p>
            <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name">
            <div class="d-flex justify-content-between align-items-center">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {APIGetPlants} from '@/http/APIService';
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
      types: ['Shrub', 'Tree', 'Annual', 'Perennial']
    };
  },
  created() {
    this.fetchPlants();
  },
  methods: {
    fetchPlants() {
      const apiService = new APIGetPlants();
      apiService.getPlantList()
        .then(response => {
          this.plant = response.data;
          this.filteredPlants = this.plant;
          console.log("fil plant: ", this.filteredPlants);
        })
        .catch(error => {
          console.error("Failed to fetch plants:", error);
        });
    },
    filterPlants() {
      this.filteredPlants = this.plant.filter((plant) => {
        return plant.name.toLowerCase().includes(this.searchQuery.toLowerCase()) &&
               (this.selectedType ? plant.type === this.selectedType : true);
      });
    },
    getPlantDetail(plant_id) {
      router.push(`plants/${plant_id}`)
    },
    getImageUrl(relativePath) {
      return `http://127.0.0.1:8000${relativePath}`;
    }
  }
}
</script>

<style>

</style>
