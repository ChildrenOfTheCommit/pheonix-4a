import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/auth/login/Login.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/auth/register/Register.vue'),
    },
  ],
})

export default router