<template>

	<div class="car" style="width: 100%; background-color: rgb(240,240,240);">
		<!-- 	{{$route.params.id}}
	{{$route.params.index}} -->
		<!-- <h1>这里是汽车详细介绍页面</h1> -->
		<div class="car">

			<!-- <div class="car-msg" v-for="(item,index) in datas[$route.params.index].car_types" v-if="item.id==$route.params.id"> -->
			<div class="car-msg"  v-if="shop&&car">
				<div class="car-top">
					<van-nav-bar :title="car.name" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
						<img style="width: 25px;height: 10px;" src="img/more.png" @click="gotomore" slot="right" alt="">
						<van-overlay :show="show" @click="show = false">
							<div class="wrapper">
								<div class="block" />
							</div>
						</van-overlay>
					</van-nav-bar>
				</div>
				<br>
				<!-- {{item.id}} -->
				<!-- {{$route.params.index}} -->
				<div class="car-img" style="width: 100%;">
					<img style="width: 80%;" :src="car.imgs[0].img" alt="">
					<p><img style="width: 3%;" src="img/tishi.png"> <span style="font-size: 10px; ">系统所选车辆型号及颜色仅供参考，具体车辆以门店实际提供为准</span></p>
					<van-divider />

					<van-row>
						<van-col span="8">{{car.displacement}}</van-col>
						<van-col span="8">{{car.transmission_name}}</van-col>
						<van-col span="8">准乘5人</van-col>
					</van-row>
					<van-divider />
					<van-row v-for="(price,index2) in prices" v-if="car.price==price.id" type="flex" justify="space-between">
						<van-col span="16">￥<strong style=" font-size: 20px;">{{price.hour}}</strong>/小时（1小时起租）</van-col>
						<van-col span="8"><strong style="color: red;font-size: 20px;">{{price.avg}}</strong>/日均</van-col>
					</van-row>

					<van-divider />
					<!-- 减{{}} -->
					<div class="addres" style=" display: flex; width: 100%;background: #fff; ">
						<div class="addres-left" style="width: 20%; ">
							<img style="padding-top: 12px;" src="img/ditu.png" alt="">
						</div>
						<div class="site-view" style="width: 60%;">
							<p style="margin: 0;padding: 0;text-align: left;">{{shop.name}}</p>
							<p style="margin: 0;padding: 0; text-align: left;font-size: 12px;font-weight: 300;">{{shop.address}}</p>
							<p style="margin: 0;padding: 0; text-align: left;font-size: 12px;font-weight: 300;">营业时间:{{shop.from_time}}-{{shop.to_time}}</p>

							<!-- 电话按钮{{datas[index].phone}} -->
						</div>
						<div class="phone" style="width: 20%;border-left: 1px rgb(240,240,240) solid;">
							<img @click="callphone" style="width: 40%;padding-top: 12px" src="img/call.png" alt="">
						</div>
					</div>
					<br>
					<van-button @click="gotoservice" type="primary" block>联系客服,当前用户{{userinfo.id}}</van-button>
				</div>
				<div style="width: 100%;height: 80px; background-color: rgb(240,240,240);">
					<div class="togo" style="  width: 90%;   position: absolute; left: 5%; bottom: 0;">
						<van-button @click="gotuOrder($route.params.index,item.id,$route.params.days)" size="large" type="danger">立即预定</van-button>
					</div>
				</div>

			</div>


		</div>

	</div>

</template>

<script>
	import {
		carslist,
		beijing
	} from '../data.js'
	export default {
		data() {
			return {
				carslist,
				car: null,
				shop: null,
				show: false,
				goodnums: 1,
				date: '',
				minDate: new Date(2020, 0, 1),
				maxDate: new Date(2025, 10, 1),
				currentDate: new Date(),
				prices:null,
				userinfo:null,
				
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res)
				this.userinfo=res.data;
			}).catch(err=>{
				console.log("出错了");
			})
			// console.log(this.$route.params.shop_id)
			this.$api.getShopDetail({
			id:this.$route.params.shop_id
			}).then(res => {
				console.log("得到门店", res)
				this.shop = res.data
			}).catch(err => {
				console.log("出错了", err)
			})
			this.$api.getCarDetail({
				id:this.$route.params.car_id
			}).then(res => {
				console.log("得到汽车", res)
				this.car = res.data
			}).catch(err => {
				console.log("出错了", err)
			})
			this.$api.getcarprices().then(res => {
				console.log("得到汽车价格", res)
				this.prices = res.data
			}).catch(err => {
				console.log("出错了", err)
			})

		},
		methods: {
			gotomore() {
				this.$router.push("/more")
			},
			gotuOrder(index, id, days) {
				console.log(index, id)
				this.$router.push("/order/" + index + "/" + id + "/" + days)
				// 存下订单
				this.$store.commit("addGood", {
					id: id,
					index: index,
					days: days,
					num: 0

				})
			},
			formatDate(date) {
				return `${date.getMonth() + 1}/${date.getDate()}`;
			},
			onConfirm(date) {
				const [start, end] = date;
				this.show = false;
				this.date = `${this.formatDate(start)} - ${this.formatDate(end)}`;
				console.log(this.date)
			},
			onClickLeft() {
				// this.$toast('返回');
				this.$router.go(-1)
			},
			onClickRight() {
				// this.$toast('按钮');
			},
			gotoservice() {
				this.$router.push("/service")
			},
			gotoindent() {
				this.$router.push("/indent")
			},
			gotohome() {
				this.$router.push("/")
			},
			gotojuan() {
				this.$router.push("/service")
			},
			togoAgreement() {
				this.$router.push("/agreement")
			},
			togocall() {
				this.$router.push("/call")
			},
			goToHome() {
				this.$router.push('/')
			},
			goToCart() {
				this.$router.push('/cart')
			},
			showPopup() {
				this.show = true
			},
			addGoodToCart() {
				this.$toast('加入购物车');
				console.log(this.datas.product_info);
				this.$store.commit("addGood", {
					id: this.datas.product_info.product_id,
					img: this.datas.goods_info[0].img_url,
					name: this.datas.product_info.name,
					price: this.datas.goods_info[0].market_price,
					num: this.goodnums,

				})
			},
			callphone(){
				this.$toast(this.shop.phone)
			}
			

		}


	}
</script>

<style scoped="scoped" lang="less">
	.car-img .van-button--primary {
		color: #000;
		background-color: white;
		border: 1px solid white;
	}
</style>
