import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunchView from '@/views/TheLunchView.vue'
import TheLottoView from '@/views/TheLottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'lunch',
    component: TheLunchView
  },
  {
    path: '/lotto/6',
    name: 'lotto',
    component: TheLottoView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
