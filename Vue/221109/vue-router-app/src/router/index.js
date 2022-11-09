import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'


Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    // lazy-loding 방식
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView,
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
      console.log('이미 로그인 함')
      next({ name: 'home' })
      } else {
      next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//  const isLoggedIn = false

// //  const authPages = ['hello']
//  const allowAllPages = ['login']

// //  const isAuthRequired = authPages.includes(to.name)
//  const isAuthRequired = !allowAllPages.includes(to.name)

//  if (isAuthRequired && !isLoggedIn) {
//   console.log('Login으로 이동!')
//   next({ name: 'login' })
//  } else {
//   console.log('to로 이동!')
//   next()
//  }
// })



export default router
