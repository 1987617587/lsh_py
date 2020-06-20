import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Cart from '../views/Cart.vue'
import Detail from '../views/Detail.vue'
import Mine from '../views/Mine.vue'
import Search from '../views/Search.vue'

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
    path: '/category',
    name: 'category',
    component: Category,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: Detail
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
	meta:{
		tabbar:true
	}
  }
]

const router = new VueRouter({
  routes
})

export default router
