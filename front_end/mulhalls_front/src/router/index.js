import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthUser from '@/components/customer/authUser.vue'
import RegisterCustomer from "@/components/customer/registerUser.vue"
import registerEmp from "@/components/employee/registerEmp.vue";
import authEmp from "@/components/employee/authEmp.vue";
import mainMenu from "@/components/mainMenu.vue";

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
      {
          path: '/mainMenu',
          name: 'mainMenu',
          component: mainMenu
      },

  ]
})

export default router
