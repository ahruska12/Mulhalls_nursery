<template>

    <div class="container">
      <div class="row align-items-center justify-content-center">
        <div class="col-12 col-sm-6 col-md-4 col-lg-4">
          <div class="card mx-auto shadow">
            <div class="card-body">
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
                <div type="button" class="btn btn-primary col-4" @click="register">Not a member? <b>Register Here</b></div>
                <br>
                <div type="button" class="btn btn-primary col-4" @click="empLogin">Employee Login</div>




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
        login() {
          // checking if the input is valid
          if (this.$refs.form) {
            this.loading = true;

            apiService.findCustomerAccount(this.credentials.username).then(response => {
              this.stored_info = response.data;
            })
                .catch(error => {
                  console.error(error);
                });

            //hash password
            bcrypt.hash(this.credentials.password, 10, (err, hash) => {
              if (err) {
                console.error('error hashing password: ', err);
              }
              else {
                bcrypt.compare(this.credentials.password, this.stored_info.customer_password, (err, result) => {
                  if (err) {
                    console.error('error comparing passwords: ', err);
                    // Handle error appropriately
                  } else {
                    if (result) {
                      this.pwMatch = true;

                      this.credentials.password = this.stored_info.customer_password;

                      apiService.authenticateLogin(this.credentials).then((res) => {
                        localStorage.setItem('token', res.data.token);
                        localStorage.setItem('isAuthenticated', JSON.stringify(true));
                        localStorage.setItem('log_user', this.stored_info.customer_email);
                        router.push("/mainMenu");
                        //router.go(-1);
                        //window.location = "/"
                      }).catch(e => {
                        this.loading = false;
                        localStorage.removeItem('isAuthenticated');
                        localStorage.removeItem('log_user');
                        localStorage.removeItem('token');
                        router.go(-1);
                        this.showMsg = 'error';
                      })
                    // Proceed with authentication
                  } else {
                      this.pwMatch = false;

                      this.showMsg = "Wrong Password or Username";
                    // Handle mismatch appropriately (e.g., show error message)
                  }
                  }
                });
              }
            })
          }
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
