import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '@/views/DogView.vue'


// 로그인 여부
const isLoggedIn = false

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // 특정 route에 가드
    beforeEnter(to, form, next) {
      // 로그인 상태로 로그인에 접근
      if (isLoggedIn === true) {
        next({ name: 'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404'
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// // 전역 가드 로그인
// router.beforeEach((to, from, next) => {
//   // 로그인이 필요한 페이지
//   // const authPages = ['hello']
//   // 로그인이 필요없는 페이지
//   const allowAllPages = ['login']
//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   // 앞으로 이동할 페이지(to)가 로그인이 필요없는 지
//   const isAuthRequired = !allowAllPages.includes(to.name)
//   if (isAuthRequired && !isLoggedIn) {
//     next({ name: 'login'})
//   } else {
//     next()
//   }
//   // console.log('to', to)
//   // console.log('from', from)
//   // console.log('next', next)
// })

export default router
