<template>
	<div class="indent">
		<div class="indent-top" style="border-bottom: 1px rgb(230,230,230) solid;">
			<!-- <van-nav-bar size="large" title="验证手机号" left-text="返回" left-arrow @click-left="onClickLeft" /> -->
			<van-nav-bar size="large" title="验证手机号">
				<img @click="onClickLeft" style="width: 50%;position: relative;top: 10px; left: -8px; " slot="left" src="img/ico_back.png"
				 alt="">
				 <img @click="onClickRight" style="width: 60%;position: relative;top: 10px; left: -8px; " slot="right" src="img/gotologin.ico"
				  alt="">
			</van-nav-bar>
		</div>
		<div class="info">

			<van-cell-group>
				<van-field center placeholder="用户名/手机号/邮箱" left-icon="img/login-user.png" v-model="username" />
			</van-cell-group>
			<van-cell-group>
				<van-field center type="password" placeholder="密码" left-icon="img/login-user.png" v-model="password" />
			</van-cell-group>
			<van-cell-group>
				<van-field center type="password" placeholder="重复密码" left-icon="img/login-user.png" v-model="password2" />
			</van-cell-group>

			<van-cell-group>
				<van-field center size="large" clearable left-icon="img/login-pwd.png" placeholder="图形校验码">
					<!-- <van-button slot="button" size="small" type="primary">发送验证码</van-button>
				right-icon -->
					<img slot="right-icon" src="https://sso.wkzuche.com/member/auth_image.do?time=1578469071268" alt="" style="width: 150px;height: 30px; margin-right: 20px;">
				</van-field>
			</van-cell-group>

			<van-cell-group>
				<van-field center clearable left-icon="img/login-pwd.png" placeholder="验证码">

					<van-button slot="button" size="small" type="primary">发送验证码</van-button>
				</van-field>
			</van-cell-group>

		</div>

		<div class="next" style="width: 94%;   position: relative; left: 3%; ">
			<br>
			<br>
			<van-button @click="gotoregist"  size="large" type="danger">注册</van-button>
		</div>
		<div class="msg">
			<div class="events-agree-content" style=" padding: 10px; position: relative; left: 6%; width: 86%; color: rgb(178,178,178); font-size:14px  ; text-align: left;">
				未注册悟空租车的手机号，点击下一步时自动注册,且代表您已阅读并同意 <a style="color: #007aff;" @click="gotoagreement">《悟空用户服务协议》</a>
			</div>
		</div>



		<div class="end">
			<div class="weixin" style="padding-top: 200px; ">
				<van-divider>第三方账户登录</van-divider>
			</div>
			<van-row type="flex" justify="center">
				<van-col span="6">
					<img style="width: 50px;height: 50px;;" src="https://static.wkzuche.com/sso/member/m/images/wechat-icon.jpg" alt=""
					 @click="weixinLogin">
				</van-col>
			</van-row>
		</div>




	</div>
</template>

<script>
	export default {
		data() {
			return {
				show: false,
				login: null,
				username:"",
				password:"",
				password2:"",

			};
		},

		methods: {
			// gotoOrder(){
			// 	this.$router.push('/order')
			// },
			gotoregist(){
				this.$api.regist({
					username:this.username,
					password:this.password,
					password2:this.password2,
					
				}).then(res=>{
				
				this.$router.push("/login")
				
			}).catch(err=>{
				console.log("出错了",err)
			})
			},
			gotoagreement() {
				this.$router.push("/agreement")
			},
			onClickLeft() {
				this.$toast('返回');
				this.$router.go(-1)
			},
			onClickRight(){
				this.$toast('前往登录');
				
			},
			weixinLogin() {
				// this.$toast('跳转微信');
				if (this.$store.getters.getGoodList.length > 0) {
					this.$router.push("/order/" + this.$store.getters.getGoodList[this.$store.getters.getGoodList.length - 1].index +
						"/" + this.$store.getters.getGoodList[this.$store.getters.getGoodList.length - 1].id + "/" + this.$store.getters
						.getGoodList[this.$store.getters.getGoodList.length - 1].days)
				} else {
					this.$router.push("/carslist/0/0")
				}
				console.log(this.$store.getters.getGoodList)
				// this.$store.getters.getGoodList

			}

		}
	}
</script>

<style scoped="scoped" lang="less">
	.indent-top .van-nav-bar__title {
		font-size: 20px;
	}

	.info input {
		font-size: 16px;
		margin: 5px;

	}

	.info .van-cell {
		border-bottom: 1px rgb(230, 230, 230) solid;
	}

	.info img {
		width: 20px;
		height: 20px;
		margin-right: 10px;
	}

	.next .van-button--danger {
		background-color: rgb(240, 240, 240);
		border: none;
		border-radius: 3%;
		/* height: 40px; */
		color: rgb(178, 178, 178);
		font-size: 20px;
	}

	.weixin .van-divider {
		margin: 0;
	}
</style>
