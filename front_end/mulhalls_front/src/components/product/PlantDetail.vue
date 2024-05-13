<template>
  <div class="main-container">
    <div class="plant-detail-card">
      <h1>{{ plant.plant_name }}</h1>
      <p class="plant-type">{{ plant.plant_type }}</p>
      <p class="plant-description">{{ plant.plant_description }}</p>
      <table v-if="specialPlantInfo && Object.keys(specialPlantInfo).length > 0" class="plant-detail-card" style="alignment: center">
        <tbody>
          <tr v-for="(value, key) in specialPlantInfo" :key="key" v-if="key !== 'plant'">
            <td>{{ getPresentableKey(key) }}</td>
            <td>{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <img :src="getImageUrl(plant.plant_picture)" :alt="plant.plant_name" class="plant-picture">
      <div v-if="!isLoggedIn"><h1>Register or Log in to ask a question!</h1></div>
      <div v-if="isLoggedIn & !isEmpl">
        <button @click="toggleQuestionForm" class="question-button">{{ questionButtonLabel }}</button>
        <div v-if="isAskingQuestion" class="question-form">
          <input v-model="question" placeholder="Ask a question..." class="question-input">
          <button @click="submitQuestion(plant.plant_id)" class="submit-button">Submit</button>
        </div>
        <div v-if="msg !== '' ">
          <h3>{{msg}}</h3>
        </div>
      </div>
    </div>
  </div>

  <div class="main-container">
    <h1>Frequently Asked Questions</h1>
    <div class="frequent-questions-card">
      <div v-for="question in questions" :key="question.question_id" class="faq-card">
        <p class="question">{{ question.question }}</p>
        <p class="answer">Expert Answer: {{ question.answer }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { APIGetPlants } from "@/http/APIService.js";
import { APIQuestions } from "@/http/APIService.js";

const plantAPI = new APIGetPlants();
const questAPI = new APIQuestions();

export default {
  name: "PlantDetail",
  data() {
    return {
      plant: {},
      msg: "",
      questions: [],
      isAskingQuestion: false,
      question: "",
      questionButtonLabel: "Ask A Question",
      specialPlantInfo: {},
      keyMap: {
        'plant': 'Plant ID:',
        'is_hardy': 'Hardy:',
        'is_semi_hardy': 'Semi-Hardy:',
        'shade_tolerant': 'Shade Tolerant:',
        'heat_tolerant': 'Heat Tolerant:',
        'drought_tolerant': 'Drought Tolerant:',
        'annual_category': 'Category:',
        'perennial_category': 'Category:',
        'tree_category': 'Category:',
        'shrub_category': 'Category:'
      }
    };
  },
  mounted() {
    this.checkAuth();
    this.getPlantInfo();
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      account_info: state => state.account_info,
    }),
  },
  methods: {
    ...mapActions([
      "checkAuth",
    ]),
    async getPlantInfo() {
      const plantId = this.$route.params.plant_id;
      const plantResponse = await plantAPI.getPlantByID(plantId);
      const questionResponse = await questAPI.findQuestionByPlant(plantId);
      const specialResponse = await plantAPI.getSpecialPlantByID(plantId);
      this.plant = plantResponse.data;
      this.questions = questionResponse.data;
      this.specialPlantInfo = specialResponse.data;
    },
    getImageUrl(relativePath) {
      return `http://127.0.0.1:8000${relativePath}`;
    },
    toggleQuestionForm() {
      this.msg = "";
      this.isAskingQuestion = !this.isAskingQuestion;
      this.questionButtonLabel = this.isAskingQuestion ? "Cancel" : "Ask A Question";
    },
    submitQuestion(plantId) {
      this.msg = "";
      if (this.isEmpl) {
        this.msg = "Employees cannot submit questions!";
      } else {
        const questionInfo = {
          customer: this.account_info.customer_id,
          plant: plantId,
          question: this.question,
        };
        questAPI.askQuestion(questionInfo)
            .then(response => {
              console.log("Question submitted successfully:", response);
            })
            .catch(error => {
              console.error("Error submitting question:", error);
            });
        this.isAskingQuestion = false;
        this.question = "";
        this.questionButtonLabel = "Ask A Question";
        this.msg = "Question Submitted!";
      }
    },
    getPresentableKey(key) {
      return this.keyMap[key] || key
    },
  },
}
</script>

<style scoped>
.main-container {
  margin-top: 20px;
  padding: 20px;
  background-color: #f0f8f6; /* Light green background */
}

.plant-detail-card {
  border: 2px solid #82c785; /* Light green border */
  border-radius: 10px;
  padding: 20px;
  text-align: center;
  background-color: #fff; /* White background */
}

.plant-type {
  font-style: italic;
  color: #888;
}

.plant-description {
  margin-top: 20px;
}

.plant-picture {
  width: 100%;
  max-width: 500px;
  height: auto;
  border-radius: 10px;
  margin-top: 20px;
}

.question-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.question-form {
  margin-top: 20px;
}

.question-input {
  width: 70%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.frequent-questions-card {
  margin-top: 40px;
}

.faq-card {
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
}

.question {
  font-weight: bold;
}

.answer {
  color: #888;
}
</style>