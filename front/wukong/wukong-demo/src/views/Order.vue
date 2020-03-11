<template>


	<div class="order">
		<!-- <h1>订单</h1> -->
		<div class="order-top">
			<van-nav-bar title="订单" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="show = true" slot="right" alt="">
				<van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay>
			</van-nav-bar>

			<van-overlay :show="show" @click="show = false">


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


			</van-overlay>

			<div class="car" style="width: 100%; background-color: rgb(240,240,240);">

				<div class="car-box">
					<br>
					<!-- <div class="car-msg" v-for="(item,index) in datas[$route.params.index].car_types" v-if="item.id==$route.params.id"> -->
					<!-- <div class="car-msg" style="display: flex; margin:10%;font-size:14px ;" v-for="(item,index) in userorders" v-if="item.user == userinfo.id">
						<img v-for="(car,index1) in cars" v-if="car.id == item.cars[0]" style="width: 30%;" :src="car.imgs[0].img" alt="">
						<van-row v-for="(car,index1) in cars" v-if="car.id == item.cars[0]">
							<van-col span="24">{{car.group_id}}</van-col>
							<van-col span="24">{{car.name}}</van-col>
							<van-col span="4" offset="5">{{car.displacement}}|</van-col>
							<van-col span="4">{{car.transmission_name}}|</van-col>
							<van-col span="6">准乘5人</van-col>
							<van-col span="24">{{item.days}}天</van-col>
						</van-row>
						<br>
						<div class="days">
							{{item.days}}天
						</div>

					</div> -->
					<div v-for="(item,index) in userorders" v-if="item.user == userinfo.id"  class="vant">
					<!-- <div v-for="(price,index2) in prices" v-if="price.id == item.price" class="vant"> -->
					<div v-for="(car,index1) in cars" v-if="car.id == item.cars[0]" class="vant">
						<van-card v-for="(price,index2) in prices" v-if="price.id == car.price" 
						:num='item.days' 
					
						:price="price.day"
						 :desc="car.name" 
						 :title="car.group_id" 
						 :thumb="car.imgs[0].img">
							<div slot="tags">
								<van-tag plain type="danger">{{car.category}}</van-tag>
							</div>
							<div slot="footer">
								<van-button type="danger" size="small">删除此订单</van-button>
								<van-button type="primary" size="mini">减少天数</van-button>
								<van-button type="primary" size="mini">增加天数</van-button>
							</div>
						</van-card>
						<!-- 111 -->
					</div>
					</div>
					<br>
				</div>
				<br>
				<!-- 		<div class="money" v-for="(car,index1) in cars" v-if="car.id == item.cars[0]" >
					<van-submit-bar :price="summoney()*car.price" button-text="提交订单" />
				</div> -->
				<div class="money">
					<van-submit-bar button-text="提交订单" />
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
				datas: null,
				show: false,
				goodnums: 1,
				date: '',
				minDate: new Date(2020, 0, 1),
				maxDate: new Date(2025, 10, 1),
				currentDate: new Date(),
				userorders: null,
				userinfo: null,
				cars: null,
				prices: null,

			}
		},
		computed: {
			islog() {
				return this.$store.getters.getlog
			},

		},
		created() {
			if (!this.islog) {
				this.$router.push("/login")
			} else {
				this.$api.getUserinfo().then(res => {
					console.log("个人信息", res)
					this.userinfo = res.data;
					this.$jsCookie.set("userinfo", res.data)
					// 获取用户信息之后获取订单
					this.$api.getOrder().then(res => {
						console.log("获取用户订单信息", res)
						this.userorders = res.data
						this.$api.getcars().then(res => {
							console.log("获取车辆信息", res)
							this.cars = res.data
							// 获取价格
							this.$api.getcarprices({
							}).then(res => {
								console.log("得到价格", res)
								this.prices = res.data
							}).catch(err=>{
								console.log("出错了", err);
							})

						}).catch(err => {
							console.log("出错了", res);
						})

					}).catch(err => {
						console.log("出错了", res);
					})
				}).catch(err => {
					console.log("出错了");
				})
			}




		},
		methods: {
			summoney(item) {
				return this.$route.params.days * 100
				console.log(item.prices.day)
			},
			gotuOrder(index, id) {
				console.log(index, id)
				this.$router.push("/order/" + index + "/" + id)
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


		}


	}
</script>

<style>
	* {
		margin: 0;
		padding: 0;
	}

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
</style>
