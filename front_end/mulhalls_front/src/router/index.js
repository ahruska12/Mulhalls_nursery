import { createRouter, createWebHistory } from 'vue-router'
import AuthUser from '@/components/customer/authUser.vue'
import RegisterCustomer from "@/components/customer/registerUser.vue"
import registerEmp from "@/components/employee/registerEmp.vue";
import authEmp from "@/components/employee/authEmp.vue";
import PlantList from "@/components/PlantList.vue";
import home from "@/components/Home.vue";
import PlantDetail from "@/components/product/PlantDetail.vue";
import QuestionList from "@/components/product/QuestionList.vue";
import AddPlant from "@/components/product/AddPlant.vue";

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
      {
          // added question list
          path: '/questions',
          name: 'QuestionList',
          component: QuestionList,
      },
      {
          // added question detail
          path: '/plants/:plant_id',
          name: 'PlantDetail',
          component: PlantDetail,
      },
      {
          // added addPlant page
          path: '/add/plant',
          name: 'AddPlant',
          component: AddPlant,
      },
  ]
})


export default router
