<template>
  <div class="main-container-questions">
    <button @click="showQuestions" class="button">{{list}}</button>
    <div v-if="!current_list">
      <div v-for="data in combinedData" v-bind:key="data.question_id" class="card">
        <div class="card-body">
        <h1 class="card-title">{{ data.plant.plant_name }}</h1>
        <h3 class="card-text">{{ data.question }}</h3>
        <img :src="getImageUrl(data.plant.plant_picture)" :alt="data.plant.plant_name">
          <br>
        <button @click="answerQuestion(data.question_id)">Answer</button>
        <div v-if="currentAnsweringID === data.question_id">
          <input v-model="answer" placeholder="Answer me" />
          <button @click="submitQuestion(data.question_id)">Send</button>
        </div>
        </div>
      </div>
    </div>
  </div>
  <div class="main-container-questions">
    <div v-if="current_list">
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

//may be slowed down because it is grabbing all questions first then all unanswered next, possible way to speed it up if needed

export default {
  name: 'QuestionList',
  data: () => ({
    //flag for filter on what questions are shown
    current_list: false,
    //message for current list
    list: "Unanswered Questions",
    //array of all questions in db
    all_questions: [],
    //array of all unanswered questions in db
    un_questions: [],
    //array of all plant ids associated with unanswered questions array
    plant_ids: [],
    //array of all plant ids associated with all questions array
    all_plant_ids: [],
    //array of all plants associated with unanswered questions array
    plants: [],
    //array of all plants associated with all questions array
    all_plants: [],
    //array of unanswered questions with associated plant record nested inside
    combinedData: [],
    //array of all questions with associated plant record nested inside
    combinedAllData: [],
    //the question ID of the question currently being answered
    currentAnsweringID: "",
    //is the question being answered now?
    currentAnswerFlag: false,
    //current answer being typed in
    answer: "",
    //array to be used in the API call to answer the question
    answer_info: {'question_id': "",
                  'employee_id': "",
                  'answer': ""},
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
    //split into two methods one that calls all plants and one that calls unanswered plants?
    async getAllQuestions() {
      //list all questions in db
      const result = await apiService.listQuestions();
      //list all unanswered questions in db
      const need_answer = await apiService.listUnQuestions(1);
      //un answered questions
      this.un_questions = need_answer.data;
      //all questions
      this.all_questions = result.data;
      //for each question out of the unanswered questions
      for (let question of this.un_questions) {
        //populate array with all plants used in unanswered questions arrary
        this.plant_ids.push(question.plant);
      }
      //get all plants used from array above
      const pResult = await apiPService.getPlantByArr(this.plant_ids);
      //array of plant objects used above
      this.plants = pResult.data;
      //combine plants used in unanswered questions with unanswered questions array
      this.combinedData = this.un_questions.map(question => {
        return {
          ...question,
          plant: this.plants.find(plant => plant.plant_id === question.plant)
        };
      });
      for (let question of this.all_questions) {
        //populate array with all plants used in all questions array
        this.all_plant_ids.push(question.plant);
      }
      //get all plants used from array above
      const pAllResult = await apiPService.getPlantByArr(this.all_plant_ids);
      //array of plant objects used above
      this.all_plants = pAllResult.data;
      //combine plants used in all questions with all questions array
      this.combinedAllData = this.all_questions.map(question => {
        return {
          ...question,
          plant: this.all_plants.find(plant => plant.plant_id === question.plant)
        };
      });
    },
    //change answer id to current question being answered
    answerQuestion(question_id) {
      if (!this.currentAnswerFlag) {
        this.currentAnsweringID = question_id;
        this.currentAnswerFlag = true;
      }
      else {
        this.currentAnsweringID = "";
        this.currentAnswerFlag = false;
      }
    },
    submitQuestion(question_id) {
      //set the array for answering the question
      this.answer_info.question_id = question_id;
      this.answer_info.employee_id = this.account_info.employee_id;
      this.answer_info.answer = this.answer;
      console.log("ans info ", this.answer_info)
      //answer the question
      apiService.answerQuestion(this.answer_info)
      .then(response => {
      console.log("Answer submitted successfully:", response);
      //reset answer variables
      this.answer = '';
      this.currentAnsweringID = "";
      //refresh all questions
      this.getAllQuestions();
      })
      .catch(error => {
      console.error("Error submitting answer:", error);
      });
    },
    showQuestions() {
      //button to filter between all questions and unanswered
      this.current_list = !this.current_list;
      if (this.current_list) {
        this.list = "Unanswered Questions";
      }
      else {
        this.list = "All Questions";
      }
      console.log("oooo", this.list)
    },
    getImageUrl(relativePath) {
      return `http://127.0.0.1:8000${relativePath}`;
    }
  },
  mounted() {
    this.checkAuth();
    this.getAllQuestions();
    console.log("ans: ", this.currentAnsweringID)
  }
}
</script>

<style scoped>

</style>