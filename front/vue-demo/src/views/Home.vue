<template>
	<div class="home">
		<img alt="Vue logo" src="../assets/logo.png">
		<!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
		<div>
			<button @click="getCategories()">发起请求</button>
			<br>
			<label for="">分类名</label><input type="text" v-model="categoryname">
			<br>
			<button @click="createCategory()">发起创建分类请求</button>
			<br>
			<label for="">需要修改的分类id</label><input type="text" v-model="oldcategoryid">
			<br>
			<label for="">新的分类名</label><input type="text" v-model="newcategoryname">
			<br>
			<button @click="updateCategory()">发起修改分类请求</button>
			<br>
			<label for="">用户名</label><input type="text" v-model="username">
			<br>
			<label for="">密码</label><input type="text" v-model="password">
			<br>
			<button @click="getToken()">请求Token</button>
		</div>
		<div class="categories">

		</div>
	</div>
</template>

<script>
	// @ is an alias to /src
	// import HelloWorld from '@/components/HelloWorld.vue'

	export default {
		name: 'Home',
		data() {
			return {
				username: "",
				password: "",
				categoryname: "",
				newcategoryname:"",
				oldcategoryid:"",

			}
		},
		components: {
			// HelloWorld
		},
		methods: {
			getCategories() {
				this.$api.getCategorylist().then(res => {
					console.log("得到分类列表", res);
				}).catch(err => {
					console.log("发生错误", err);
				})
				// console.log("测试函数")
				// this.$http({
				// 	method: 'get',
				// 	url: 'http://127.0.0.1:8000/categories/'
				// }).then(res => {
				// 	console.log("得到分类列表", res);
				// }).catch(err => {
				// 	console.log("发生错误", err);
				// })
			},
			getToken() {
				this.$api.getToken({
					username: this.username,
					password: this.password
				}).then(res => {
					console.log("得到Token", res);
					this.$jsCookie.set("refresh",res.data.refresh)
					this.$jsCookie.set("access",res.data.access)
				}).catch(err => {
					console.log("发生错误", err);
				})
				// console.log("请求token")
				// this.$http({
				// 	method: 'post',
				// 	url: 'http://127.0.0.1:8000/token_login/',
				// 	data: {
				// 		username: this.username,
				// 		password: this.password
				// 	}
				// }).then(res => {
				// 	console.log("得到Token", res);
				// }).catch(err => {
				// 	console.log("发生错误", err);
				// })

			},
			createCategory() {
				if (this.categoryname != "") {
					this.$api.crerteCategory({
						name: this.categoryname
					}).then(res => {
						console.log("添加分类成功", res);
					}).catch(err => {
						console.log("发生错误", err);
					})
					// this.$http({
					// 	method: 'post',
					// 	url: 'http://127.0.0.1:8000/categories/',
					// 	data: {
					// 		name: this.categoryname
					// 	},
					// 	headers: {
					// 		// Authorization:'Basic YWRtaW46MTIzNDU2'
					// 		Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMzcyNzU5LCJqdGkiOiJlYjM3ZjE2NjVjMmE0NWEzODg2N2NkODBhMWVlMmQ4MCIsInVzZXJfaWQiOjF9.WqaY6ZIQPn5TkQ3c8Qe3cKVlKtgMrIT9GPvm7ql5mxQ'
					// 	}
					// }).then(res => {
					// 	console.log("添加分类成功", res);
					// }).catch(err => {
					// 	console.log("发生错误", err);
					// })
				} else {
					console.log("分类名不能为空");
				}
			},
			updateCategory(){
				if(this.oldcategoryid!="" & this.newcategoryname!=""){
					this.$api.modifyCategory({
						name: this.newcategoryname,
						id:this.oldcategoryid
					}).then(res => {
						console.log("修改分类成功", res);
					}).catch(err => {
						console.log("发生错误", err);
					})
				}
				else{
					console.log("不允许为空")
				}
			}
		}
	}
</script>
