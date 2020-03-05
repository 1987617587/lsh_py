<template>
	
	<div>
		<van-nav-bar
		  title="标题"
		  left-text="返回"
		  left-arrow
		  @click-left="onClickLeft"
		/>
		<label for="">用户名</label><input type="text" v-model="username">
		<br>
		<label for="">密码</label><input type="text" v-model="password">
		<br>
		<button @click="getToken()">请求Token</button>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				username: "",
				password: "",

			}
		},
		created() {
		},
		methods: {
			getToken() {
				this.$api.getToken({
					username: this.username,
					password: this.password
				}).then(res => {
					console.log("得到Token", res);
					this.$jsCookie.set("refresh", res.data.refresh)
					this.$jsCookie.set("access", res.data.access)
					this.$router.push("/")
				}).catch(err => {
					console.log("发生错误", err);
					this.$toast("用户名或密码错误")
				})
				
			},
			onClickLeft(){
				this.$router.push("/")
			}
		}
	}
</script>

<style>
</style>
