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
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('log_user');
      localStorage.removeItem('token');

      if (state.isEmpl) {
        localStorage.removeItem('isAdmin');
      }

      commit('SET_LOGIN_STATE', { isLoggedIn: false, isEmpl: false });
      commit('SET_ACCOUNT_INFO', { email: "", username: "Guest", account_info: [] });
      commit('SET_LOADING', false);

      router.push('/');
      console.log("Logged out");
    },
    async checkAuth({ commit, state }) {
      console.log("checkAuth v2 called")
      if (localStorage.getItem('isAuthenticated')) {
        state.isLoggedIn = true;
        state.email = localStorage.getItem('log_user');
        if (localStorage.getItem('isAdmin') === "1") {
        state.isEmpl = true;
        }
      }
      console.log("not empl")
      try {
        let account_info;
        console.log("inside try")
        if (state.isEmpl) {
          const response = await apiService.findEmployeeAccount(state.email);
          state.account_info = response.data;
          console.log("account info", account_info)
          commit('SET_ACCOUNT_INFO', {
            email: state.email,
            username: state.account_info.employee_first_name,
            account_info: state.account_info
          });
        } else if (state.isLoggedIn) {
          console.log("inside find account cust")
          const response = await apiService.findCustomerAccount(state.email);
          state.account_info = response.data;
          console.log("account info", account_info)
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
    // ... other actions ...
  }
});
