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
    <div v-if="isLoggedIn">
      <button @click="askQuestion()">Ask A Question!</button>
      <div v-if="beingAsked">
        <p>{{question}}</p>
        <input v-model="question" placeholder="What's your question?"/>
        <button @click="submitQuestion(plant.plant_id)">Send</button>
      </div>
    </div>
  </div>
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
    //if a question is being asked currently
    beingAsked: false,
    //current question - customer_id, plant_id, question
    question_info: {'customer': "",
               'plant': "",
               'question': ""},
    //question holder
    question: "",
    //used to store any sys messages
    msg: "",
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
    async getPlantInfo() {
      const plant_id = this.$route.params.plant_id;
      const pResult = await plantAPI.getPlantByID(plant_id)
      const qResult = await questAPI.findQuestionByPlant(plant_id)
      this.plant = pResult.data;
      this.questions = qResult.data;
      console.log("plant: ", this.plant)
      console.log("quest: ", this.questions)
    },
    askQuestion() {
      console.log(this.beingAsked)
      this.beingAsked = !this.beingAsked;
    },
    submitQuestion(plant_id) {
      if (this.isEmpl) {
        this.msg = "Employees cannot submit questions!"
      }
      else {
        this.question_info.customer = this.account_info.customer;
        this.question_info.plant = plant_id;
        this.question_info.question = this.question;
        questAPI.askQuestion(this.question_info)
            .then(response => {
              console.log("Question submitted successfully:", response);
            })
        this.question_info.customer = "";
        this.question_info.plant = "";
        this.question_info.question = "";
      }
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