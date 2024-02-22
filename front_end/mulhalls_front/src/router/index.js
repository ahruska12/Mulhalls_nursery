import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthUser from '@/components/authUser.vue'
import Register from "@/components/register.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/AuthUser',
        name: 'authUser',
        component: AuthUser
    },
      {
          path: '/RegisterUser',
          name: 'RegisterUser',
          component: Register
      },
  ]
})

export default router
