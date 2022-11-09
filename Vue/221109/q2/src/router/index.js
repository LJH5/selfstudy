import Vue from 'vue'
import VueRouter from 'vue-router'
import FirstView from '@/views/FirstView'
import SecondView from '@/views/SecondView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: FirstView
  },
  {
    path: '/second',
    name: 'second',
    component: SecondView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
