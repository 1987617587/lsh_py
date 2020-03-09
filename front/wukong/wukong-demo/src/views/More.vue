<template>

	<div class="more">
		<div class="more-top">
			<van-nav-bar title="更多" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="show = true" slot="right" alt="">
				<van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay>
			</van-nav-bar>



		</div>
		<div class="more-body">
			<!-- 加跳转 to="index"  -->
			<van-cell-group>
				<van-cell @click="togocall" center style="height: 60px;font-size: 16px;" value="联系我们" is-link />
				<van-cell @click="togoAgreement" center style="height: 60px;font-size: 16px;" value="用车服务协议" is-link />

			</van-cell-group>

			<!-- <img src="img/more.png" @click="show = true" alt=""> -->
			<van-overlay :show="show" @click="show = false">
				<!-- <div class="wrapper"> -->


				<div class="block">
					<br>
					<van-row @click="gotohome" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/home.png" alt="">
						</van-col>
						<van-col span="12"><h4>返回首页</h4></van-col>
					</van-row>
					<van-row @click="gotoindent" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/myident.png" alt="">
						</van-col>
						<van-col span="12"><h4>我的订单</h4></van-col>
					</van-row>
					<van-row @click="gotojuan" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/morejuan.png" alt="">
						</van-col>
						<van-col span="12"><h4>优惠卷</h4></van-col>
					</van-row>
					<van-row @click="gotoservice" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/myservice.png" alt="">
						</van-col>
						<van-col span="12"><h4>客服中心</h4></van-col>
					</van-row>
				</div>
				<!-- </div> -->

			</van-overlay>



		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				show: false,

			}
		},
		methods: {
			onClickLeft() {
				// this.$toast('返回');
				this.$router.go(-1)
			},
			onClickRight() {
				// this.$toast('按钮');
			},
			gotoservice(){
				this.$router.push("/service")
			},
			gotoindent(){
				this.$router.push("/indent")
			},
			gotohome(){
				this.$router.push("/")
			},
			gotojuan(){
				this.$router.push("/service")
			},
			togoAgreement(){
				this.$router.push("/agreement")
			},
			togocall(){
				this.$router.push("/call")
			}
		}
	}
</script>

<style scoped="scoped" lang="less">
	/* 	.wrapper {
		position: absolute;
		top: 50px;
		right: 0px;
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100px;
		width: 200px;
		z-index: 10
	} */

	.block {
		top: 48px;
		right: 16px;
		border-radius: 8%;
		position: absolute;
		width: 160px;
		height: 160px;
		background-color: #fff;
		z-index: 10
	}

	.van-nav-bar {
		width: 100%;
		height: 46px;
		color: red;
		z-index: 10;
	}

	.van-hairline--bottom {
		width: 100%;
		height: 46px;
		color: red;
		z-index: 10;
	}
	h4{
		margin: 0;padding: 0;
		font-size: 20px;
		font-weight: 500;
	}
</style>
