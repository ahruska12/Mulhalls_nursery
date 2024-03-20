<template>
    <div class="container-fluid">
        <div class="row align-items-center justify-content-center">
            <div class="col col-12 col-sm-6 col-md-10 col-lg-6">
                <div class="card">
                    <div class="card-header">Create Customer Account</div>
                    <div v-if="showMsg === 'Passwords Must Match'" class="alert alert-danger" role="alert">
                    Passwords do not match
                    </div>
                    <div v-if="showMsg === 'Email already exists'" class="alert alert-danger" role="alert">
                    That email is already registered
                    </div>
                    <div class="p-2"> </div>

                    <div class="card-body">
                        <div class="row align-items-center justify-content-center" v-if="loading">
                        </div>
                        <form v-else ref="form">
                            <div class="container-fuild">
                                    <div class="form-group row justify-content-left py-2">
                                        <label class="col-4">Email</label>
                                        <div class="col col-8">
                                            <input name="email" v-model="credentials.customer_email" type="text" class="form-control-sm form-control">
                                        </div>
                                    </div>
                                    <div class="form-group row justify-content-end py-2">
                                        <label class="col-4">Password</label>
                                        <div class="col col-8">
                                            <input v-model="credentials.customer_password" type="password" class="form-control-sm form-control">
                                        </div>
                                    </div>
                                    <div v-if="this.valid === true" class="alert alert-danger" role="alert">
                                      GREEN CHECK
                                    </div>
                                    <div v-if="this.valid === false" class="alert alert-danger" role="alert">
                                      RED X
                                    </div>
                                    <div class="form-group row justify-content-left py-2">
                                        <label class="col-4">Re-enter password</label>
                                        <div class="col col-8">
                                            <input v-model="credentials.password2" type="password" class="form-control-sm form-control">
                                        </div>
                                    </div>
                                   <div class="form-group row justify-content-left py-2">
                                        <label class="col-4">First Name</label>
                                        <div class="col col-8">
                                            <input v-model="credentials.customer_first_name" type="text" class="form-control-sm form-control">
                                        </div>
                                    </div>
                                    <div class="form-group row justify-content-left py-2">
                                        <label class="col-4">Last Name</label>
                                        <div class="col col-8">
                                            <input v-model="credentials.customer_last_name" type="text" class="form-control-sm form-control">
                                        </div>
                                    </div>
                                    <div class="row justify-content-around">
                                        <div type="button" class="btn btn-secondary col-6" @click="login">Back to Login</div>
                                       <div type="button" class="btn btn-primary col-4" @click="registerUser">Register</div>
                                   </div>
                           </div>
                        </form>
                   </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>

  import router from '../../router/index.js';
  import {APIService} from '../../http/APIService.js';
  import bcrypt from "bcryptjs";
  const apiService = new APIService();

  export default {
    name: 'RegisterCustomer',

    data: () => ({
      credentials: {},
      customer_password: "",
      repassword: "",
      valid: true,
      showMsg: '',
      passwordMsg: "",
      loading: false,
      showPassword: false,
    }),
    methods: {
      registerUser() {
        if (this.credentials.customer_password === this.credentials.password2) {
          bcrypt.hash(this.credentials.customer_password, 10, (err, hash) => {
            if (err) {
              console.error('error hashing password: ', err);
              return;
            }

            this.credentials.customer_password = hash;

            apiService.registerUser(this.credentials).then(response => {
              if (response.status === 201) {
                this.movie = response.data;
                this.showMsg = "User Registered";
                router.push('/AuthUser/');
              } else {
                this.showMsg = "Email already exists";
              }
            }).catch(error => {
              if (error.response.status === 401) {
                router.push("/AuthUser");
              } else if (error.response.status === 400) {
                this.showMsg = "Email already exists";
              }
            });
          })
        }
        else {
          this.showMsg = "Passwords Must Match"
        }
      },
      login() {
        router.push("/authUser");
      },
      comparePasswords() {
        if (this.credentials.customer_password !== this.credentials.password2) {
          this.valid = false;
        } else {
          this.valid = true;
        }
      }
    },
    watch: {
      'credentials.customer_password': function(newVal, oldVal) {
        this.comparePasswords();
      },
      'credentials.password2': function(newVal, oldVal) {
        this.comparePasswords();
      }
    },
  }
</script>