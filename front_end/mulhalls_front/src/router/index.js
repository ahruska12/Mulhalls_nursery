import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

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
          name: 'AuthUser',
          component: () => import('../components/authUser')
      },
      {
          path: '/RegisterUser',
          name: 'RegisterUser',
          component: () => import('../components/register')
      },
  ]
})

export default router
