import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 引入请求http模块
import Axios from 'axios'
// 将Axios注册进Vue的原型 以后再项目中就可以使用 this.$http
Vue.prototype.$http = Axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
