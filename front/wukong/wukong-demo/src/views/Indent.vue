<template>
	<div class="indent">
		<div class="indent-top" style="border-bottom: 1px rgb(230,230,230) solid;">
			<!-- <van-nav-bar size="large" title="验证手机号" left-text="返回" left-arrow @click-left="onClickLeft" /> -->
			<van-nav-bar size="large" title="验证手机号"  >
				<img  @click="onClickLeft" style="width: 50%;position: relative;top: 10px; left: -8px; " slot="left" src="img/ico_back.png" alt="">
				</van-nav-bar>
		</div>
		<div class="info">

			<van-cell-group>
				<van-field center placeholder="手机号" left-icon="img/login-user.png" />
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
			<van-button size="large" type="danger">下一步</van-button>
		</div>
		<div class="msg" >
			<div class="events-agree-content" style=" padding: 10px; position: relative; left: 6%; width: 86%; color: rgb(178,178,178); font-size:14px  ; text-align: left;">
				未注册悟空租车的手机号，点击下一步时自动注册,且代表您已阅读并同意 <a style="color: #007aff;" href="https://m.wkzuche.com/#/profile/more/user_agreement?flag=1">《悟空用户服务协议》</a>
			</div>
		</div>
		
		
		
		<div class="end"  >
			<div class="weixin" style="padding-top: 200px; " >
				<van-divider>第三方账户登录</van-divider>
			</div>
			<van-row type="flex" justify="center">
			  <van-col span="6">
				  <img style="width: 50px;height: 50px;;" src="https://static.wkzuche.com/sso/member/m/images/wechat-icon.jpg" alt="" @click="weixinLogin">
			  </van-col>
			</van-row>
		</div>
		
		
		
		
	</div>
</template>

<script>
	export default {
		data() {
		    return {
		      show: false
		    };
		  },
		methods: {
			onClickLeft() {
				this.$toast('返回');
				this.$router.go(-1)
			},
			weixinLogin(){
				this.$toast('跳转微信');
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
	.weixin .van-divider{
		margin: 0;
	}
	
</style>
