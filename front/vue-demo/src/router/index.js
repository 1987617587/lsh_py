import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Goods from '../views/Goods.vue'
import Login from '../views/Login.vue'
import Regist from '../views/Regist.vue'
import UserCenter from '../views/UserCenter.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/categories/:id/',
    name: 'Category',
    component: Category
  },
  {
    path: '/goods/',
    name: 'Goods',
    component: Goods
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/regist/',
    name: 'Regist',
    component: Regist
  },
  {
    path: '/UserCenter/',
    name: 'UserCenter',
    component: UserCenter
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
