<template>

</template>

<script>
import {mapState} from "vuex";
import {APIGetPlants, APIQuestions} from "@/http/APIService.js";
const apiService = new APIQuestions()
const apiPService = new APIGetPlants()

export default {
  name: "QuestionDetail",
  data: () => ({
    question_id: "",
    question: [],
    plant: [],
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
    async getQuestion() {

    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>