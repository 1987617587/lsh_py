import axios from 'axios'
import jsCookie from 'js-cookie'
// axios.defaults.baseURL = 'http://127.0.0.1:8000'
// 允许手机访问
axios.defaults.baseURL = 'http://192.168.0.103:8000'

// 拦截请求
axios.interceptors.request.use(function(config) {
	// 在发起请求之前可以对请求进行处理  其中config就是请求中的config参数
	// config.headers.Authorization="Basic YWRtaW46MTIzNDU2"
	config.headers.Authorization = `Bearer ${jsCookie.get('access')}`;
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
		window.location.href = "#/login/"
		// 删除之前的cookie信息
		jsCookie.remove("access")
		jsCookie.remove("refresh")
	}
	if (error.response.status == 403) {
		console.log('权限不足，无法修改')
		// 跳转到登录页面
		window.location.href = "#/login/"
		// 删除之前的cookie信息
		jsCookie.remove("access")
		jsCookie.remove("refresh")
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

export const getCategoryDetail = (param) => {
	console.log("getCategoryDetail执行了")

	return axios.get(`/categories/${param.id}`)
}


export const crerteCategory = (param) => {
	console.log("crerteCategory执行了", "参数", param)
	return axios.post("/categories/", param)
	// return axios.post("/categories/", param, {
	// 	headers: {
	// 		Authorization: 'Basic YWRtaW46MTIzNDU2'
	// 		// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
	// 	}
	// })
}
export const modifyCategory = (param) => {
	console.log("modifyCategory执行了", "参数", param)
	return axios.put(`/categories/${param.id}/`, param, {
		// headers: {
		// 	Authorization: 'Basic YWRtaW46MTIzNDU2'
		// 	// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
		// }
	})
}


export const getToken = (param) => {
	console.log("getToken执行了", "参数", param)
	// return axios({
	// 	method: 'post',
	// 	url: '/token_login/',
	// 	data: param,
	// })
	return axios.post('/token_login/', param)

}
