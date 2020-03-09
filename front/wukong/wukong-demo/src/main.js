import Vue from 'vue'
import '../src/assets/new_file.css'
import App from './App.vue'
import router from './router'
import store from './store'
import Vant from 'vant';
import 'vant/lib/index.css';
import { Dialog } from 'vant';

// 全局注册
Vue.use(Dialog);
Vue.use(Vant);
Vue.config.productionTip = false

// 引入axios
// import axios from 'axios'
// Vue.prototype.$http = axios

// 导入api中的所有内容
import * as api from './api'
// 将api注册进Vue的原型 以后再项目中就可以使用 this.$api
Vue.prototype.$api = api


// 将js-cookie模块注册 Vue原型
import jsCookie from "js-cookie"
Vue.prototype.$jsCookie = jsCookie


import BaiduMap from 'vue-baidu-map'

Vue.use(BaiduMap, {
  // ak 是在百度地图开发者平台申请的密钥 详见 http://lbsyun.baidu.com/apiconsole/key */
  ak: 'fHrNQj6DHTjZtfTvfqbsuvTzKc5V9SBl'
})


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
