<template>
<div class="main-container">
  <div class="plant-detail-card">
    <h1>{{plant.plant_name}}</h1>
    <br>
    <p>{{plant.plant_type}}</p>
    <br>
    <p>{{plant.plant_type}}</p>
    <br>
    <p>{{plant.plant_description}}</p>
  </div>
  <div v-if="isLoggedIn"></div>
</div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import {APIGetPlants} from "@/http/APIService.js";
import {APIQuestions} from "@/http/APIService.js";
const plantAPI = new APIGetPlants();
const questAPI = new APIQuestions()

export default {
  name: "PlantDetail",
  data: () => ({
    //dont think we will need this
    plant_id: "",
    //current plant
    plant: {},
    //answered questions for plant (FAQ)
    questions: {},
  }),
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
    async getPlantInfo(plant_id=2) {
      const pResult = await plantAPI.getPlantByID(plant_id)
      const qResult = await questAPI.findQuestionByPlant(plant_id)
      this.plant = pResult.data;
      this.questions = qResult.data;
      console.log("plant: ", this.plant)
      console.log("quest: ", this.questions)
    }
  },
  mounted() {
    this.checkAuth();
    this.getPlantInfo();
  }
}

</script>

<style scoped>

</style>