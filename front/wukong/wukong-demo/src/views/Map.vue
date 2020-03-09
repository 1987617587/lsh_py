<template>
	<div>
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

			<!-- <img src="img/more.png" @click="show = true" alt=""> -->
			<van-overlay :show="show" @click="show = false">
				<!-- <div class="wrapper"> -->


				<div class="block">
					<br>
					<van-row @click="gotohome" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/home.png" alt="">
						</van-col>
						<van-col span="12">
							<h4>返回首页</h4>
						</van-col>
					</van-row>
					<van-row @click="gotoindent" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/myident.png" alt="">
						</van-col>
						<van-col span="12">
							<h4>我的订单</h4>
						</van-col>
					</van-row>
					<van-row @click="gotojuan" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/morejuan.png" alt="">
						</van-col>
						<van-col span="12">
							<h4>优惠卷</h4>
						</van-col>
					</van-row>
					<van-row @click="gotoservice" type="flex" justify="center">
						<van-col span="8">
							<img style="width: 50%" src="img/myservice.png" alt="">
						</van-col>
						<van-col span="12">
							<h4>客服中心</h4>
						</van-col>
					</van-row>
				</div>
				<!-- </div> -->

			</van-overlay>



			<!-- 我是地图demo1 -->
			<label>关键词：<input v-model="keyword"></label>
			<br>
			<label>地区：<input v-model="location"></label>
			<baidu-map>
				<bm-view class="map"></bm-view>
				<bm-local-search :keyword="keyword" :auto-viewport="true" :location="location"></bm-local-search>
			</baidu-map>

		</div>
	</div>

</template>

<script>
	export default {
		name: "map",

		data() {
			return {
				location: '北京',
				keyword: '王府井租车',
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

<style>
	.map {
		width: 100%;
		height: 400px;
	}
</style>
