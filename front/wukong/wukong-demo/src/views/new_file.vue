<template>
	<div class="home" style="height: 600px;">
		<div class="top" style="height: 374px;width: 374px; ">
			<van-swipe :autoplay="3000" indicator-color="white">
				<van-swipe-item><img @click="gotocoupon" src="https://img-zuche.oss-cn-beijing.aliyuncs.com/banner/2019/0924/cce59db4-81c3-41d5-aedc-b6891ae9a4c1.jpg"
					 style="width: 100%;" alt=""></van-swipe-item>
				<van-swipe-item><img @click="gotocoures" src="https://img-zuche.oss-cn-beijing.aliyuncs.com/banner/2019/0516/ee788c6b-8189-4e9c-a568-177584e34467.jpg"
					 style="width: 100%;" alt=""></van-swipe-item>
			</van-swipe>
		</div>
		<div class="bc" style="height: 300px;width: 374px; background-color: rgb(240,240,240); " >
			<div class="hone-search" style="border-radius: 3% ; position: relative; top: -170px;left : 5%;height:360px;width: 90%; background-color: white;">
				<br>
				<div class="time" style="font-size: 14px; font-weight: 300; ">
					<br>
					<van-row>
						<van-col span="8">取车时间</van-col>
						<van-col span="8">3天</van-col>
						<van-col span="8">还车时间</van-col>
					</van-row>
					<br>
					<van-row>
						<van-col span="8">
							<p style="font-size: 20px;font-weight: 700;">1月9日</p>
						</van-col>
						<van-col span="8"></van-col>
						<van-col span="8">
							<p style="font-size: 20px;font-weight: 700;">1月12日</p>
						</van-col>
					</van-row>
					<br>
					<van-row>
						<van-col span="8">周四 10:00</van-col>
						<van-col span="8"><img style=" position: relative; top:-20px; height: 20px;width: 60px; " src="img/goto.png" alt=""></van-col>
						<van-col span="8">周日 10:00</van-col>
					</van-row>
					<van-divider />
					<van-row>
						<van-col span="6" offset="1">取还城市</van-col>
						<van-col span="14" offset="1">取还地址</van-col>
					</van-row>
					<div class="address" style="font-size:12px;font-weight: 700;">
						<van-row>
							<van-col span="8" >
								<van-cell title="广州" is-link arrow-direction="down" />
							</van-col>
							<van-col span="13" offset="1">
								<van-cell title="请选择" is-link arrow-direction="down" />
							</van-col>
						</van-row>
					</div>
					
					<van-divider />
				</div>
				<div class="togo" style="width: 90%;   position: relative; left: 5%; ">
					<van-button size="large" type="danger">去租车</van-button>
				</div>
				<br>
				<div class="other" @click="gotocoupon" >
					<van-row type="flex">
					  <van-col span="2"><img style="width:100%; " src="img/juan.png" alt=""></van-col>
					  <van-col span="22">新用户福利升级，首单立减100二单再减50</van-col>
					</van-row>
			
				</div>
				
			</div>
			
			
			
			<div @click="guide" class="guide"  style=" z-index: 1;  position: relative; top:-150px; width: 100%; height: 100px;">
			<div class="guide" style="   position: relative; top:-150px; width: 100%; height: 100px; background-color: #fff; ">
				<van-overlay :show="show1">
					<div class="block">
						<img style="width: 100%;" src="https://static.wkzuche.com/H5/images/h5/activity/y2019/newUserFourth/1.jpg" alt="">
					</div>
				</van-overlay>
			</div>
			</div>
			
			
			
			<div @click="guide" class="guide" style="   position: relative; top:-150px; width: 100%; height: 70px; background-color: #fff; ">
				<br>
				<van-row span="24">
					<van-col  span="4"><img  src="img/guide.png" alt="" style="padding-left:20px ; width:60%"></van-col>
					<van-col span="16">
						<!-- <div class="msg"> -->
							<van-row type="flex" style="font-size:16px;font-weight: 600;">
								<van-col span="7">
									<p>租车指南</p>
								</van-col>
							</van-row>
							<van-row type="flex" style="font-size: 13px;font-weight: 300;">
								<van-col span="22">
									<p >租车、取还车、押金及服务分分钟搞定</p>
								</van-col>
							</van-row>
						<!-- </div> -->
					</van-col>
					<van-col span="4" >
						<van-cell title="" is-link />
					</van-col>
				</van-row>
			
			</div>
			

			
		</div>
		<div class="foot" style="width: 100%; height: 200px; background-color: #fff;">
			<div class="foot-top" style=" position: relative; top: -100px;  font-size:1px; height: 60px; ">
				<van-row>
					<van-col span="8">
						<div>
							<img style="width: 30%;" src="https://img-zuche.oss-cn-beijing.aliyuncs.com/banner/2018/0926/226a9b32-440d-4d56-a1dc-d9c9d7f76447.png">
							<p>272城市</p>
							<p>16254服务网点</p>
						</div>
					</van-col>
					<van-col span="8">
						<div><img style="width: 30%;" src="https://img-zuche.oss-cn-beijing.aliyuncs.com/banner/2018/0926/8c281026-8af6-4011-abe4-0c760a9c29d3.png">
							<br>
							<p>5268车型</p>
							<p>105837车辆</p>
						</div>
					</van-col>
					<van-col span="8">
						<div><img style="width: 30%;" src="https://img-zuche.oss-cn-beijing.aliyuncs.com/banner/2018/0926/02aef3f2-290b-4c84-969a-57f57b5016b0.png">
							<br>
							<p>7*24H专属客服</p>
							<p>品质服务保障</p>
						</div>
					</van-col>
				</van-row>
		
			</div>

			<div class="foot-bottom" style=" position: relative; top: -80px;  " >
				<van-row>
					<van-col span="12"><img style="width: 70%;" src="img/download.png"></van-col>
					<van-col span="12"><img style="width: 80%;" src="img/phone.png"></van-col>
				</van-row>
			</div>
		</div>
		


	</div>
</template>

<style scoped="scoped" lang="less">
	.van-cell__title span{
		font-size: 16px
	}
	p{
		margin: 0;padding: 0;
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

<script>
	// @ is an alias to /src
	import HelloWorld from '@/components/HelloWorld.vue'

	export default {
		name: 'home',
		components: {
			HelloWorld
		},
		data(){
			return{
				show1: false,
			}
		},
		methods:{
			gotocoupon(){
				this.$router.push("/coupon")
			},
			gotocoures(){
				this.$router.push("/coures")
			},
			guide(){
				this.$toast('显示指南轮播');
				this.show1 = !this.show1
			}
			
		}
	}
</script>
