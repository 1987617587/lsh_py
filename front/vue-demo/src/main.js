import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 引入请求Http模块
// import Axios from 'axios'
// 将Axios注册进Vue的原型 以后再项目中就可以使用 this.$http
// Vue.prototype.$http = Axios

// 导入api中的所有内容
import * as api from './api'
// 将api注册进Vue的原型 以后再项目中就可以使用 this.$api
Vue.prototype.$api = api

// 将js-cookie模块注册 Vue原型
import jsCookie from "js-cookie"
Vue.prototype.$jsCookie = jsCookie


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
