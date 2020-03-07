<template>
	<div class="regist">
	
		<van-form @submit="regist">
		  <van-field
		    v-model="username"
		    name="用户名"
		    label="用户名"
		    placeholder="用户名"
		    :rules="[{ required: true, message: '请填写用户名' }]"
		  />
		  <van-field
		    v-model="password"
		    type="password"
		    name="密码"
		    label="密码"
		    placeholder="密码"
		    :rules="[{ required: true, message: '请填写密码' }]"
		  />
		  <van-field
		    v-model="password2"
		    type="password"
		    name="重复密码"
		    label="重复密码"
		    placeholder="重复密码"
		    :rules="[{ required: true, message: '请填写重复密码' }]"
		  />
		  <div style="margin: 16px;">
		    <van-button round block type="info" native-type="submit">
		      提交
		    </van-button>
		  </div>
		</van-form>
		
		
	</div>
</template>

<script>
	export default{
		data(){
			return{
				username:"",
				password:"",
				password2:"",
			}  
		},
		methods:{

			regist(){
				this.$api.regist({
					username:this.username,
					password:this.password,
					password2:this.password2
				}).then(res=>{
					this.$router.push("/login/")
				}).catch(err=>{
					this.$toast("注册失败")
				})
			}
		}
	}
</script>

<style>
</style>
