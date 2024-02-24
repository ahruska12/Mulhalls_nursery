<template>
    <div class="container-fluid">
        <div class="row align-items-center justify-content-center">
            <div class="col col-12 col-sm-6 col-md-10 col-lg-6">
                <div class="card">
                    <div class="card-header">Create Customer Account</div>
                    <div v-if="showMsg === 'error'" class="alert alert-danger" role="alert">
                    Invalid username or password. Please Try again.
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

  import router from '../router';
  import {APIService} from '../http/APIService';
  const apiService = new APIService();

  export default {
    name: 'RegisterCustomer',

    data: () => ({
      credentials: {},
      customer_password: "",
      repassword: "",
      valid: true,
      showMsg: '',
      loading: false,
      rules: {
        customer_password: [
          v => !!v || "Password is required",
          v => (v && v.length > 7) || "The password must be longer than 7 characters"
        ],
        customer_email: [
          v => !!v || "Email is required"
        ],
        repassword: [
          v => (v === this.customer_password) || 'Passwords must match'
        ]
      },
      showPassword: false,
    }),
    methods: {
      register() {
       apiService.registerUser(this.credentials).then(response => {
         console.log(this.credentials)
          if (response.status === 201) {
            this.movie = response.data;
            this.showMsg = "";
            router.push('/AuthUser/');
          }else{
            this.showMsg = "error";
          }
        }).catch(error => {
          if (error.response.status === 401) {
            router.push("/AuthUser");
          }else if (error.response.status === 400) {
            this.showMsg = "error";
            console.log(this.credentials)
          }
        });
      },
      login() {
        router.push("/authUser");
      }
    },
    computed: {
      passwordConfirmationRule() {
        return (this.customer_password === this.repassword) || 'Password must match'
    }
    }
  }
</script>