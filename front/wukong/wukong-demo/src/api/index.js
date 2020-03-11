import axios from 'axios'
import jsCookie from 'js-cookie'
axios.defaults.baseURL = 'http://127.0.0.1:8000'
// 允许手机访问

// axios.defaults.baseURL = 'http://192.168.1.104:8000'

// 拦截请求
axios.interceptors.request.use(function(config) {
	// 在发起请求之前可以对请求进行处理  其中config就是请求中的config参数
	// config.headers.Authorization="Basic YWRtaW46MTIzNDU2"
	// config.headers.Authorization = `Bearer ${jsCookie.get('access')}`;
	if (jsCookie.get('access')) {
		config.headers.Authorization = `Bearer ${jsCookie.get('access')}`;
	}
	return config
}, function(error) {
	return Promise.reject(error)
})
// 拦截相应
axios.interceptors.response.use(function(response) {
	return response
}, function(error) {
	if (error.response.status == 401) {
		console.log('认证失败,请先登录')
		// 跳转到登录页面
		window.location.href = "/#/login"
		// 删除之前的cookie信息
		jsCookie.remove("access")
		jsCookie.remove("refresh")
		jsCookie.remove("username")
	}
	if (error.response.status == 403) {
		console.log('权限不足，无法修改')
		// 跳转到登录页面
		window.location.href = "/#/login"
		// 删除之前的cookie信息
		jsCookie.remove("access")
		jsCookie.remove("refresh")
		jsCookie.remove("username")
	}
	return Promise.reject(error)
})

export const getCategorylist = () => {
	console.log("getCategorylist执行了")
	// return axios({
	// 	method: 'get',
	// 	url: '/categories/'
	// })
	return axios.get("/categories/")
}

// export const getCategoryDetail = (param) => {
// 	console.log("getCategoryDetail执行了")
// 
// 	return axios.get(`/categories/${param.id}`)
// }

// 获取所有门店信息
export const getshops = (param) => {
	console.log("getshops执行了")

	return axios.get("/shops/")
}
// 获取单个门店信息
export const getShopDetail = (param) => {
	console.log("getShopDetail执行了")

	return axios.get(`/shops/${param.id}`)
}
// 获取商品对应的分类信息
export const getCategories = (param) => {
	console.log("getCategories执行了")

	return axios.get("/categories/")
}

// 获取所有商品列表
export const getcars = (param) => {
	console.log("getcars执行了")

	return axios.get("/cars/")
}
// 获取单个商品信息
export const getCarDetail = (param) => {
	console.log("getCarDetail执行了")

	return axios.get(`/cars/${param.id}`)
}
// 获取所有汽车平均价格
export const getcarprices = (param) => {
	console.log("getcarprices执行了")

	return axios.get("/prices/")
}
// 获取单个汽车价格信息
export const getPriceDetail = (param) => {
	console.log("getPriceDetail执行了")

	return axios.get(`/prices/${param.id}`)
}
// 创建订单
export const crerteOrder = (param) => {
	console.log("crerteOrder执行了", "参数", param)
	return axios.post("/orders/", param,)
	// return axios.post("/categories/", param, {
	// 	headers: {
	// 		Authorization: 'Basic YWRtaW46MTIzNDU2'
	// 		// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
	// 	}
	// })
}
// 查看用户自己的订单
export const getOrder = (param) => {
	console.log("getOrder执行了", "参数", param)
	return axios.get("/userorders/")
}
// 用户修改自己的订单
export const updateOrder = (param) => {
	console.log("updateOrder执行了", "参数", param)
	return axios.patch(`/orders/${param.id}/`,param)
}
// 删除自己的订单
export const delOrder = (param) => {
	console.log("delOrder执行了", "参数", param)
	return axios.delete(`/orders/${param.id}/`)
}


// 查看用户所有订单
export const getOrders = (param) => {
	console.log("getOrders执行了", "参数", param)
	return axios.get("/orders/")
}
// export const modifyCategory = (param) => {
// 	console.log("modifyCategory执行了", "参数", param)
// 	return axios.put(`/categories/${param.id}/`, param, {
// 		// headers: {
// 		// 	Authorization: 'Basic YWRtaW46MTIzNDU2'
// 		// 	// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
// 		// }
// 	})
// }
// 
// 登录
export const getToken = (param) => {
	console.log("getToken执行了", "参数", param)

	return axios.post('/login/', param)

}
// 
// 注册
export const regist = (param) => {
	return axios.post("/users/", param, )
}

//获取用户信息
export const getUserinfo = (param)=>{
	return axios.get("/userinfo/",param,)
}
// 用户修改个人信息
export const modifyUserInfo = (param)=>{
	// console.log("提交更改数据",param);
	let id = param.userinfo.id
	console.log(id,"===",param);
	return axios.patch(`users/${id}/`,param.userinfo,)
}


// 
// 
// export const getUserinfo = (param)=>{
// 	return axios.get("/userinfo/",param,)
// }
// 
// getDateDiff(startDate, endDate) {
// 		var startTime = new Date(Date.parse(startDate.replace(/-/g, "/"))).getTime();
// 		var endTime = new Date(Date.parse(endDate.replace(/-/g, "/"))).getTime();
// 		var dates = Math.abs((startTime - endTime)) / (1000 * 60 * 60 * 24);
// 		return dates;
// 	},
// 	timeTransform(str) {
// 		// var str = "2010-08-01";
// 
// 		// 转换日期格式
// 
// 		str = str.replace(/-/g, '/'); // "2010/08/01";
// 		// 创建日期对象
// 
// 		var datetime = new Date(str);
// 
// 		// 加一天
// 
// 		// date.setDate(date.getDate() + 1);
// 		return datetime
// 	},
//
