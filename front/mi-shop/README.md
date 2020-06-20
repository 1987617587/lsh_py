# mi-shop

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

```
# 页面分析
1. 首页
2. 分类
3. 购物车
4. 我的
5. 搜索
6. 详情


路由传参三种方式

http://192.168.10.10/detail/101   101为变量 
http://192.168.10.10/detail/:id   $route.params.id  

http://192.168.10.10/login?redirect=/cart   $route.query.redirect

通过meta :{
	auth:true,
	tabbar:true
}   $route.meta.auth 



VUE全家桶
vue.js 
vue-router  一个路由地址可以返回对应数据  
			router-link router-view
			params  query  meta
vuex  数据状态管理器  同步不同组件之间数据 
	  在详情页加入购物车 
	  在购物车页面展示购物车
	  
	  vuex中还是内存数据 要么存储本地 要么同步网络




```
