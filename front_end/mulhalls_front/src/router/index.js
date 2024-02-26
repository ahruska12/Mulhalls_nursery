import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthUser from '@/components/authUser.vue'
import RegisterCustomer from "@/components/registerUser.vue"
import registerEmp from "@/components/registerEmp.vue";
import authEmp from "@/components/authEmp.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
          path: '/',
          name: 'home',
          component: HomeView
      },
      {
          path: '/authUser',
          name: 'authUser',
          component: AuthUser
      },
      {
          path: '/registerUser',
          name: 'registerCustomer',
          component: RegisterCustomer
      },
      {
          path: '/authEmp',
          name: 'authEmployee',
          component: authEmp
      },
      {
          path: '/registerEmp',
          name: 'registerEmployee',
          component: registerEmp
      },

  ]
})

export default router
