<template>
<div v-for="data in combinedAllData" v-bind:key="data.question_id" class="card">
        <div class="card-body">
          <h1 class="card-title">{{ data.plant.plant_name }}</h1>
          <h3 class="card-text">{{ data.question }}
          <br>
            {{data.answer}}
          </h3>
          <img :src="getImageUrl(data.plant.plant_picture)" :alt="data.plant.plant_name">
      </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import {APIQuestions} from "@/http/APIService.js";
import {APIGetPlants} from "@/http/APIService.js";
import router from "@/router/index.js";
const apiService = new APIQuestions()
const apiPService = new APIGetPlants()


export default {
  name: 'custQuestions',
  data: () => ({
    all_questions: {},
    combined_data: {},
    plants: {},
    plant_ids: [],
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
    async getAllQuestions() {
      await this.checkAuth();
      //list all questions in db
      console.log("cust info", this.account_info);
      const result = await apiService.findQuestionByUser(this.account_info.customer_id);
      //all questions
      this.all_questions = result.data;
      //get all plants used from array above
      for (let question of this.all_questions) {
        //populate array with all plants used in unanswered questions arrary
        this.plant_ids.push(question.plant);
      }
      const pResult = await apiPService.getPlantByArr(this.plant_ids);
      //array of plant objects used above
      this.plants = pResult.data;
      this.combined_data = this.all_questions.map(question => {
        return {
          ...question,
          plant: this.plants.find(plant => plant.plant_id === question.plant)
        };
      });
      console.log("final: ", this.combined_data)
    },
  },
  mounted() {
    this.getAllQuestions();
  }
}
</script>

<style scoped>

</style>