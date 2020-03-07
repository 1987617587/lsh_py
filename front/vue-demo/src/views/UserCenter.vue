<template>
	<div class="usercenter">
		<h1>用户中心</h1>
		<div v-if="userinfo">			
			<div>
				<h2>修改信息</h2>
				<!-- 输入手机号，调起手机号键盘 -->
				<van-field v-model="userinfo.username" type="tel" label="用户名" />
				<van-field v-model="userinfo.tel" type="tel" label="手机号" />
				<van-field v-model="userinfo.password" type="password" label="密码" />
				<van-field v-model="userinfo.email" type="email" label="邮箱" />
				
				 <van-button @click="modify" round block type="info" native-type="submit">
				      修改信息
				 </van-button>
			</div>
		</div>
		<div v-else>
			<van-button plain  @click="gotologin"  type="primary">前往登录</van-button>
		</div>
	</div>
</template>
<script>
	export default{
		methods:{
			modify(){
				console.log("++");
				this.$api.modifyUserInfo({
					userinfo:this.userinfo
				}).then(res=>{
					console.log("更改成功",res);
					this.$toast("更改成功")
				}).catch(err=>{
					console.log("更改出错",err);
				})
			},
			gotologin(){
				this.$router.push("/login")
			}
		},
		data(){
			return{
				 userinfo:null,
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res)
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("出错了");
			})
		},
		filters:{
			dataFormat(date){
				date = new Date(date)
				console.log(date, typeof(date));
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
	}
	
	
</script>

<style>
</style>
