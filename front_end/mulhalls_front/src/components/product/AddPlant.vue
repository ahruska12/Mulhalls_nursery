<template>
  <h1>New Plant</h1>
<div class="main-container">
  <div class="enter-info">
  <h2>Name</h2>
  <input v-model="plant_info.plant_name" placeholder="Name">
  </div>
  <div class="enter-info">
    <h2>Type</h2>
    <select v-model="current_type">
    <option v-for="type in plant_type">{{type}}</option>
  </select>
  </div>
  <div class="enter-info">
    <h2>Color</h2>
    <input v-model="plant_info.plant_color" placeholder="Color">
  </div>
  <div class="enter-info">
    <h2>Description</h2>
    <input v-model="plant_info.plant_description" placeholder="Description">
  </div>
  <div class="enter-info">
    <h2>Size</h2>
    <input v-model="plant_info.plant_size" placeholder="Size">
  </div>
  <div class="enter-info">
    <h2>Picture</h2>
    <input type="file" @change="inputImage($event)">
  </div>
</div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "AddPlant",
  data: () => ({
    current_type: "",
    //to change inputs based on plant type
    plant_type: ["Shrub", "Perenial", "Annual", "Tree"],
    //used for api call to add plant
    plant_info: {'plant_type': "",
                 'plant_name': "",
                 'plant_size': "",
                 'plant_color': "",
                 'plant_description': "",
                 'plant_picture': "",
                 'department_id': ""},
    //used to store any sys messages
    msg: "",
  }),
  methods: {
    inputImage(event) {
      console.log(event)
      console.log(event.target)
      const file = event.target.files[0];
      console.log(file)
    }
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
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>