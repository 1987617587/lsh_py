<template>
	<div class="coupon" style="width: 375px;height: 1645px; ">
		<div class="box">

			<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/detail1.png" alt="">
		</div>

		<div @click="juan4" class="juan" style=" position: relative; top:-520px; left: 86px;  width: 200px;height: 92px;">
			<van-overlay :show="show4">
				<div class="block">
					<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/4.jpg" alt="">
				</div>
			</van-overlay>
		</div>
		<div @click="juan3" class="juan" style=" position: relative; top:-735px; left: 86px;  width: 200px;height: 92px;">
			<van-overlay :show="show3">
				<div class="block">
					<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/3.jpg" alt="">
				</div>
			</van-overlay>
		</div>
		<div @click="juan2" class="juan" style=" position: relative; top:-950px; left: 86px;  width: 200px;height: 92px;">
			<van-overlay :show="show2">
				<div class="block">
					<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/2.jpg" alt="">
				</div>
			</van-overlay>
		</div>
		<div @click="juan1" class="juan" style=" position: relative; top:-1165px; left: 86px;  width: 200px;height: 92px;">
			<!-- <van-button type="primary" text="显示遮罩层" @click="show = true" /> -->
			<van-overlay :show="show1">
				<div class="block">
					<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/1.jpg" alt="">
				</div>
			</van-overlay>
		</div>
		<div @click="go" class="juan" style=" position: relative; top:-596px; left: 76px;  width: 214px;height: 46px;">
		</div>


	</div>



</template>

<script>
	export default {
		data() {
			return {
				show1: false,
				show2: false,
				show3: false,
				show4: false,
			};
		},
		methods: {
			juan1() {
				this.show1 = !this.show1

			},
			juan2() {
				this.show2 = !this.show2

			},
			juan3() {
				this.show3 = !this.show3

			},
			juan4() {
				this.show4 = !this.show4

			},
			go() {
				this.$router.push("/");
			},

		}
	}
</script>

<style scoped="scoped" lang="less">
	* {
		margin: 0;
		padding: 0;
	}


	.block {
		position: absolute;
		top: 150px;
		left: 10px;
		width: 352px;
		height: 338px;
		background-color: #fff;
	}
</style>
