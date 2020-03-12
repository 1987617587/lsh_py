import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Indent from '../views/Indent.vue'
import Mine from '../views/Mine.vue'
import Service from '../views/Service.vue'
import Login from '../views/Login.vue'
import Regist from '../views/Regist.vue'
import UserCenter from '../views/UserCenter.vue'
import More from '../views/More.vue'
import Call from '../views/Call.vue'
import Agreement from '../views/Agreement.vue'
import Problem from '../views/Problem.vue'
import Coupon from '../views/Coupon.vue'
import Course from '../views/Course.vue'
import Feedback from '../views/Feedback.vue'
import Detail from '../views/Detail.vue'
import Carslist from '../views/Carslist.vue'
import Order from '../views/Order.vue'
import Screen from '../views/Screen.vue'
import Searchlist from '../views/Searchlist.vue'

import Map from '../views/Map.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/indent',
    name: 'indent',
    component: Indent,
	meta:{
		auth:true
	}
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/regist',
    name: 'regist',
    component: Regist
  },
  {
    path: '/usercenter',
    name: 'usercenter',
    component: UserCenter
  },
  {
    path: '/coupon',
    name: 'coupon',
    component: Coupon
  },
  {
    path: '/detail/:shop_id/:car_id/:days',
    name: 'detail',
    component: Detail
  },
  {
    path: '/order',
    name: 'order',
    component: Order
  },
  {
    path: '/carslist/:dateto/:dateend/:addres',
    name: 'carslist',
    component: Carslist
  },
  {
    path: '/searchlist/:class/:search',
    name: 'searchlist',
    component: Searchlist
  },
  
  {
    path: '/coures',
    name: 'coures',
    component: Course
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: Feedback
  },
  
  {
    path: '/more',
    name: 'more',
    component: More
  },
  {
    path: '/call',
    name: 'call',
    component: Call
  },
  {
    path: '/agreement',
    name: 'agreement',
    component: Agreement
  },
  {
    path: '/problem',
    name: 'problem',
    component: Problem
  },
  {
    path: '/screen',
    name: 'screen',
    component: Screen
  },
  {
    path: '/map',
    name: 'map',
    component: Map
  },
  
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
	meta:{
		tabbar:true,
	}
  },
  {
    path: '/service',
    name: 'service',
    component: Service,
	meta:{
		tabbar:true
	}
  },

  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

// 路由守卫 导航守卫
// 进去和离开路由之前
router.beforeEach(function(t,f,n){
	
	console.log(t,f,n)
	// n为执行跳转括号内可以给跳转路由页面地址
	// n();
	
	// 如果跳转的页面需要认证则跳往认证页面
	if(t.meta.auth){
		n("/login")
	}else{
		n()
	}
	
	// if(t.meta.auth){
	// 	n()
	// 	// let r = localStorage.getItem("login")
	// 	// if(r){
	// 	// 	n()
	// 	// }else{
	// 	// 	// 未登录强行跳转到我的登录页面
	// 	// 	n("/login?t="+t.path)
	// 	// }
	// }else{
	// 	n()
	// }
		
})
export default router
