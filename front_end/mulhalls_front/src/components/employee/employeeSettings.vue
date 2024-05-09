<template>
<div class="home-container">
    <h1 class="home-title">Mulhall's Plant Support System Settings</h1>
    <button @click="backup">Backup!!!</button>
</div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import {APIService} from "@/http/APIService.js";
const API = new APIService;
export default {
  name: "employeeSettings",
  data() {
    return {
      user_id: "",
    };
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.isLoggedIn,
      isEmpl: state => state.isEmpl,
      username: state => state.username,
      loading: state => state.loading,
      account_info: state => state.account_info,
    }),
  },
  methods: {
    ...mapActions([
      'checkAuth',
    ]),
    backup() {
      API.backupData(this.account_info.employee_id)
    }
  },
  mounted() {
    this.checkAuth();
  }
}
</script>

<style scoped>

</style>