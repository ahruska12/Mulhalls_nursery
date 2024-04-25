import { createRouter, createWebHistory } from 'vue-router'
import AuthUser from '@/components/customer/authUser.vue'
import RegisterCustomer from "@/components/customer/registerUser.vue"
import registerEmp from "@/components/employee/registerEmp.vue";
import authEmp from "@/components/employee/authEmp.vue";
import PlantList from "@/components/PlantList.vue";
import home from "@/components/Home.vue";
import QuestionDetail from "@/components/product/QuestionDetail.vue";
import QuestionList from "@/components/product/QuestionList.vue";

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
          path: '/question-detail/:question_id',
          name: 'QuestionDetail',
          component: QuestionDetail,
      },
  ]
})


export default router
