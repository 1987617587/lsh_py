import axios from 'axios'
import jsCookie from 'js-cookie'
axios.defaults.baseURL = 'http://127.0.0.1:8000'

// 拦截请求
axios.interceptors.request.use(function(config){
	// 在发起请求之前可以对请求进行处理  其中config就是请求中的config参数
	// config.headers.Authorization="Basic YWRtaW46MTIzNDU2"
	config.headers.Authorization=`Bearer ${jsCookie.get('access')}`;
	return config
},function(error){
	return Promise.reject(error)
})
// 拦截相应
axios.interceptors.response.use(function(response){
	return response
},function(error){
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


export const crerteCategory = (param) => {
	console.log("crerteCategory执行了", "参数", param)
	return axios.post("/categories/",param)
	// return axios.post("/categories/", param, {
	// 	headers: {
	// 		Authorization: 'Basic YWRtaW46MTIzNDU2'
	// 		// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
	// 	}
	// })
}
export const modifyCategory = (param) => {
	console.log("modifyCategory执行了", "参数", param)
	return axios.put(`/categories/${param.id}/`,param, {
		headers: {
			Authorization: 'Basic YWRtaW46MTIzNDU2'
			// Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
		}
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
