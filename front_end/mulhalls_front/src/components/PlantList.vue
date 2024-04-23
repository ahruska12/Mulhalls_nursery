<template>
  <div class="plant-list">
    <h2>Plant Catalog</h2>
    <ul v-if="plants.length">
      <li v-for="plant in plants" :key="plant.id">
        <h3>{{ plant.name }}</h3>
        <p>Price: {{ plant.price }}</p>
        <p>Description: {{ plant.description }}</p>
        <!-- Add more plant details as needed -->
      </li>
    </ul>
    <p v-else>No plants found.</p>
  </div>
</template>

<script>
export default {
  name: 'PlantList',
  data() {
    return {
      plants: []
    }
  },
  mounted() {
    this.fetchPlants();
  },
  methods: {
    async fetchPlants() {
      try {
        const response = await fetch('https://your-backend-api.com/plants');
        if (!response.ok) {
          throw new Error('Failed to fetch plants');
        }
        const data = await response.json();
        this.plants = data;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>

<style scoped>
/* Add component-specific styles here */
.plant-list {
  margin: 20px;
}

.plant-list h2 {
  color: #333;
}

.plant-list ul {
  list-style-type: none;
  padding: 0;
}

.plant-list li {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.plant-list li:last-child {
  border-bottom: none;
}
</style>
