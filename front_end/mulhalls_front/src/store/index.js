// store/index.js
import { createStore } from 'vuex';
import { APIService } from "@/http/APIService.js";
import router from "@/router/index.js";
const apiService = new APIService();

export default createStore({
  state() {
    return {
      isLoggedIn: false,
      isEmpl: false,
      email: "",
      username: "Guest",
      account_info: [],
      loading: false, // Added loading state
    };
  },
  mutations: {
    SET_LOGIN_STATE(state, { isLoggedIn, isEmpl }) {
      state.isLoggedIn = isLoggedIn;
      state.isEmpl = isEmpl;
    },
    SET_ACCOUNT_INFO(state, { email, username, account_info }) {
      state.email = email;
      state.username = username;
      state.account_info = account_info;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    // ... other mutations ...
  },
  actions: {
    logout({ commit, state }) {
      commit('SET_LOADING', true);
      localStorage.removeItem('1100101657896245');
      localStorage.removeItem('log_user');
      localStorage.removeItem('token');

      if (state.isEmpl) {
        localStorage.removeItem('4125879635');
      }

      commit('SET_LOGIN_STATE', { isLoggedIn: false, isEmpl: false });
      commit('SET_ACCOUNT_INFO', { email: "", username: "Guest", account_info: [] });
      commit('SET_LOADING', false);

      router.push('/');
    },
    async checkAuth({ commit, state }) {
      if (localStorage.getItem("1100101657896245") === "548792615836") {
        state.isLoggedIn = true;
        state.email = localStorage.getItem('log_user');
        if (localStorage.getItem("4125879635") === "112544879526328") {
        state.isEmpl = true;
        }
      }
      try {
        let account_info;
        if (state.isEmpl) {
          const response = await apiService.findEmployeeAccount(state.email);
          state.account_info = response.data;
          commit('SET_ACCOUNT_INFO', {
            email: state.email,
            username: state.account_info.employee_first_name,
            account_info: state.account_info
          });
        } else if (state.isLoggedIn) {
          const response = await apiService.findCustomerAccount(state.email);
          state.account_info = response.data;
          commit('SET_ACCOUNT_INFO', {
            email: state.email,
            username: state.account_info.customer_first_name,
            account_info: state.account_info
          });
        }
      } catch (error) {
        console.error(error);
      }
      console.log("email", state.email)
      console.log("username", state.username)
      console.log("acct", state.account_info)
    },
  }
});
