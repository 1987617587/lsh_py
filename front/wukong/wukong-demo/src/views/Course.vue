<template>
	<div class="coupon" style="width: 375px;height: 1645px; ">
		<div class="box">
		<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/zhimaDepoist/detail.jpg" alt="">
		</div>
		<div @click="go" class="juan" style=" position: relative; top:-165px; left: 126px;  width: 118px;height: 32px;">
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

<style>
</style>
