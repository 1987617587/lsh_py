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
		
		
		
		<div class="bc" style="height: 300px;width: 374px; background-color: rgb(240,240,240); ">
			<div class="hone-search" style="border-radius: 3% ; position: relative; top: -170px;left : 5%;height:360px;width: 90%; background-color: white;">
				<br>
				<div class="time" style="font-size: 14px; font-weight: 300; ">
					<br>
					<van-row>
						<van-col span="8">取车时间</van-col>
						<!-- <van-col span="8">{{date}}天</van-col> -->
						<van-col span="8"></van-col>
						<van-col span="8">还车时间</van-col>
					</van-row>
					<br>
					<van-row>
						<van-col span="8">
							<p style="font-size: 20px;font-weight: 700;">{{dateto}}</p>
						</van-col>
						<van-col span="8"></van-col>
						<van-col span="8">
							<p style="font-size: 20px;font-weight: 700;">{{dateend}}</p>
						</van-col>
					</van-row>
					<br>
					<van-row>
						<!-- <van-col  span="8">周一 10:00</van-col> -->
						<van-col span="8">
							<van-cell title="出发" :value="dateto" @click="showto = true" />
							
							<van-calendar v-model="showto" @confirm="onConfirmto" />
						</van-col>
						<van-col span="8"><img style=" position: relative; top:-20px; height: 20px;width: 60px; " src="img/goto.png" alt=""></van-col>
						<!-- <van-col span="8">周四 10:00</van-col> -->
						<van-col span="8">
							<van-cell title="结束" :value="dateend" @click="showend= true" />
							
							<van-calendar v-model="showend" @confirm="onConfirmend" />
						</van-col>
					</van-row>
					<van-divider />
					<van-row>
						<van-col span="6" offset="1">取还城市</van-col>
						<van-col span="14" offset="1">取还地址</van-col>
					</van-row>
					<div class="address" style="font-size:12px;font-weight: 700;">
						<van-row>
							<van-col span="8">
								<van-cell title="北京" is-link arrow-direction="down" />
							</van-col>
							<van-col @click="zuobiao" span="13" offset="1">
								<van-cell title="王府井" is-link arrow-direction="down" />
							</van-col>
						</van-row>
					</div>

					<van-divider />
				</div>
				<div class="togo" style="width: 90%;   position: relative; left: 5%; ">
					<van-button @click="gotoCarslist(dateto,dateend)" size="large" type="danger">去租车</van-button>
				</div>
				<br>
				<br>
				<div class="other" @click="gotocoupon">
					<van-row type="flex">
						<van-col span="2"><img style="width:100%; " src="img/juan.png" alt=""></van-col>
						<van-col span="22">新用户福利升级，首单立减100二单再减50</van-col>
					</van-row>

				</div>

			</div>

			<!-- <div @click="guide" class="guide" style="   position: relative; top:-120px; width: 375px; height: 100px; background-color: #0000FF;">
				
			</div>
 -->







			<div style="   position: relative; top:-140px; width: 100%; height: 70px; background-color: #fff; ">

				<van-overlay :show="show1">
					<div class="block" style=" position: absolute; top: 120px; left: 35px; height: 300px;width: 300px;">
						<div class="imgs" style=" width:300px;height: 320px; background-color: #fff; ">
							<van-swipe :autoplay="30000" style=" width: 300px; height: 350px;" indicator-color="white">

								<van-swipe-item>
									<img style="width: 100%;" src="https://m.wkzuche.com/www/images/guide_pic1.1140447.png" alt="">
									<p>身份认证</p>
									<p style="font-size: 13px;padding: 10px;">门店人员将与您确认身份证、驾照及信用卡（免除全部押金、或线上支付押金的客户无需携带信用卡），并讲解合同</p>
								</van-swipe-item>
								<van-swipe-item>
									<img style="width: 100%;" src="https://m.wkzuche.com/www/images/guide_pic2.3318ab3.png" alt="">
									<p>透明验车</p>
									<p style="font-size: 13px;padding: 10px;">门店人员将陪同您一起查看租赁车辆的外观及内饰情况</p>
								</van-swipe-item>
								<van-swipe-item>
									<img style="width: 100%;" src="https://m.wkzuche.com/www/images/guide_pic3.a38c660.png" alt="">
									<p>押金提车</p>
									<p style="font-size: 13px; padding: 10px;">缴纳一定金额的车辆押金后，您即可提车离店</p>
								</van-swipe-item>
								<van-swipe-item>
									<img style="width: 100%;" src="https://m.wkzuche.com/www/images/guide_pic4.13a03bb.png" alt="">
									<p>轻松用车</p>
									<p style="font-size: 13px;padding: 10px;">用车中您可随时拨打门店电话或悟空官网客服400-0515-507解决旅途中发生的意外情况</p>
								</van-swipe-item> -->

							</van-swipe>
							<van-icon @click="guide" size="36" color="#fff" name="cross" />

						</div>


					</div>
				</van-overlay>
				<br>
				<van-row span="24">
					<van-col span="4"><img src="img/guide.png" alt="" style="  padding-left:20px ; width:60%"></van-col>
					<van-col span="16">
						<!-- <div class="msg"> -->
						<van-row type="flex" style="font-size:16px;font-weight: 600;">
							<van-col span="7">
								<p>租车指南</p>
							</van-col>
						</van-row>
						<van-row type="flex" style="font-size: 13px;font-weight: 300;">
							<van-col span="22">
								<p>租车、取还车、押金及服务分分钟搞定</p>
							</van-col>
						</van-row>
						<!-- </div> -->
					</van-col>
					<van-col span="4">
						<van-cell title="" is-link />
					</van-col>
				</van-row>

			</div>



		</div>
		<div class="foot" style="width: 100%; height: 200px; background-color: #fff;">
			<div @click="guide()" class="foot-top" style=" position: relative; top: -80px;  font-size:1px; height: 60px;">
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


			<div class="foot-bottom" style=" position: relative; top: -60px;  ">
				<van-row>
					<van-col span="12"><img style="width: 70%;" src="img/download.png"></van-col>
					<van-col span="12"><img style="width: 80%;" src="img/phone.png"></van-col>
				</van-row>
			</div>
		</div>



	</div>
</template>



<style scoped="scoped" lang="less">
	.van-cell__title span {
		font-size: 16px
	}

	p {
		margin: 0;
		padding: 0;
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
		data() {
			return {
				// nowtime:null,
				date:null,
				show1: false,
				dateto: '',
				dateend: '',
				      showto: false,
				      showend: false,
				      show: false,
				images: [
					'img/car.png',
					'img/go.png',
					'https://img.yzcdn.cn/vant/apple-1.jpg',
					'https://img.yzcdn.cn/vant/apple-2.jpg'
				]
			}
		},
		// created() {
		// 	var s2 = day2.getFullYear() + "-" + (day2.getMonth() + 1) + "-" + day2.getDate();
		// 	this.nowtime = s2
		// },
		methods: {
			formatDateto(dateto) {
			      return `${dateto.getMonth() + 1}月${dateto.getDate()}日`;
			    },
			    onConfirmto(dateto) {
			      this.showto = false;
			      this.dateto = this.formatDateto(dateto);
			  },
			  formatDateend(dateend) {
			        return `${dateend.getMonth() + 1}月${dateend.getDate()}日`;
			      },
			      onConfirmend(dateend) {
			        this.showend = false;
					// this.date = dateend.getDate() - dateto.getDate()
					// console.log(this.date)
			        this.dateend = this.formatDateend(dateend);
			    },
			zuobiao(){
				this.$toast('选择坐标');
				this.$router.push("/map")
			},
			gotoCarslist(dateto,dateend) {
				// this.$router.push("/carslist")
				if(dateto&&dateend){
					
					this.$router.push("/carslist/"+dateto+"/"+dateend)
				}else{
					this.$router.push("/carslist/0/0")
				}
			},
			gotocoupon() {
				this.$router.push("/coupon")
			},
			gotocoures() {
				this.$router.push("/coures")
			},
			guide() {
				// this.$toast('显示指南轮播');
				this.show1 = !this.show1
			}

		}
	}
</script>
