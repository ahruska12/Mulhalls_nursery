import { createRouter, createWebHistory } from 'vue-router'
import AuthUser from '@/components/customer/authUser.vue'
import RegisterCustomer from "@/components/customer/registerUser.vue"
import registerEmp from "@/components/employee/registerEmp.vue";
import authEmp from "@/components/employee/authEmp.vue";
import PlantList from "@/components/PlantList.vue";
import home from "@/components/Home.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
          // changed the home screen to mainMenu
          path: '/',
          name: 'home',
          component: home,
      },
      {
          // added plant list
          path: '/plants',
          name: 'PlantList',
          component: PlantList,
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
