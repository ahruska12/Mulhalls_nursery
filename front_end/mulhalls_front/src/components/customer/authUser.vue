<template>

    <div class="container">
      <div class="row align-items-center justify-content-center">
        <div class="col-12 col-sm-6 col-md-4 col-lg-4">
          <div class="card mx-auto shadow">
            <div class="card-body">
              <div v-if="error">Not a valid Account! Try again!</div>
              <div class="card-title"><span>Login</span></div>
              <div
                v-if="showMsg === 'Wrong Password or Username'"
                close-icon="mdi-close-circle"
                :value="true"
                class="alert alert-danger"
                role="alert"
                dense>
                Invalid email or password. Please Try again.
              </div>
              <div class="card-text pt-2">
                <div
                  class="row align-items-center justify-content-center"
                  v-if="loading">
                  <div class="progress">
                    <div class="progress-bar progress-bar-striped progress-bar-animated"
                      role="progressbar"
                      aria-valuenow="75"
                      aria-valuemin="0"
                      aria-valuemax="100"
                      style="width: 75%"
                    ></div>
                  </div>
                </div>

                <div class="col-md-10 mb-3">
                  <div class="input-group">
                    <div class="input-group-prepend">
                      <span class="input-group-text">@</span>
                    </div>
                    <input

                      v-model="credentials.username"
                      :counter="70"
                      label="Email"
                      :rules="rules.username"
                      maxlength="70"
                      required
                      type="text"
                      class="form-control mb-3"
                      placeholder="Email"
                      aria-describedby="inputGroupPrepend2"
                    />


                    <div class="w-100"></div>


                    <div class="input-group-prepend">
                      <span class="input-group-text">***</span>
                    </div>
                    <input
                      :type="showPassword ? 'text' : 'Password'"
                      v-model="credentials.password"
                      label="Password"
                      :rules="rules.password"
                      maxlength="20"
                      required
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      @click:append="showPassword = ! showPassword"
                      class="form-control"
                      placeholder="Password"
                      aria-describedby="inputGroupPrepend2"


                    />
                  </div>
                </div>


                <button ref ="form" @click.prevent="login" class="btn btn-primary">Login</button>
                <div type="button" class="btn btn-primary col-4" @click="register">Not a member? <button>Register Here</button></div>
                <br>
                <div type="button" class="btn btn-primary col-4" @click="empLogin"><button>Employee Login</button></div>




              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


  </template>


  <script>




    import router from '../../router/index.js';
    import {APIService} from '../../http/APIService.js';
    const apiService = new APIService();
    import bcrypt from 'bcryptjs'


  export default {
      name: 'authUser',

      data: () => ({
        credentials: {},
        stored_info: "",
        valid: true,
        showMsg: '',
        loading: false,
        pwMatch: false,
        error: false,
        rules: {
          username: [
            v => !!v || "Email is required",
            v => (v && v.length > 3) || "A username must be more than 3 characters long",
          ],
          password: [
            v => !!v || "Password is required",
            v => (v && v.length > 7) || "The password must be longer than 7 characters"
          ]
        },
        showPassword: false,
      }),
      methods: {
        async login() {
          if (!this.$refs.form) {
            return; // Early exit if the form reference doesn't exist
          }

          this.loading = true;

          try {
            // Fetch customer account information
            const response = await apiService.findCustomerAccount(this.credentials.username);
            this.stored_info = response.data;
            console.log("Fetched stored info: ", this.stored_info);

            // Compare the hashed password
            const result = await bcrypt.compare(this.credentials.password, this.stored_info.customer_password);
            if (result) {
              // Passwords match
              this.pwMatch = true;
              await this.handleSuccessfulLogin();
            } else {
              // Passwords do not match
              this.handleFailedLogin("Wrong Password or Username");
            }
          } catch (error) {
            console.error('Login error: ', error);
            this.handleFailedLogin('Error during login process');
            this.error = true;
          }
        },

        async handleSuccessfulLogin() {
          try {
            const res = await apiService.authenticateLogin(this.credentials);
            localStorage.setItem('isAuthenticated', JSON.stringify(true));
            localStorage.setItem('log_user', this.stored_info.customer_email);
            router.push("/");
          } catch (error) {
            this.handleFailedLogin('Authentication failed');
          }
        },

        handleFailedLogin(message) {
          this.loading = false;
          localStorage.removeItem('isAuthenticated');
          localStorage.removeItem('log_user');
          this.showMsg = message;
        },
        register() {
          router.push('/customer/registerUser')
        },
        empLogin() {
          router.push('/authEmp')
        }
      }
  }
  </script>


  <style>


  input {
      padding: 1em
  }


  form {
    display: flex;
    justify-content: center;
  }


  </style>
