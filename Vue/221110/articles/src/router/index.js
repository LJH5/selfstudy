import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '@/views/IndexView'
import CreatedView from '@/views/CreatedView'
import DetailView from '@/views/DetailView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreatedView
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
