<template>
	<div v-if="$route.params.days!='null'" class="order">
		<div class="order-top">
			<van-nav-bar title="订车" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="show = true" slot="right" alt="">
				<van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay>
			</van-nav-bar>

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

			<div class="car" style="width: 100%; background-color: rgb(240,240,240);">

				<div class="car-box">
					<br>
					<!-- <div class="car-msg" v-for="(item,index) in datas[$route.params.index].car_types" v-if="item.id==$route.params.id"> -->
					<div class="car-msg" style="display: flex; margin:10%;font-size:14px ;" v-for="(item,index) in datas[$route.params.index].car_types"
					 v-if="item.id==$route.params.id">
						<!-- {{item.id}} -->
						<img style="width: 30%;" :src="item.pics.pic1" alt="">
						<van-row>
							<br>
							<van-col span="24">{{item.car_type_name}}</van-col>
							<van-col span="4" offset="5">{{item.basics.displacement}}|</van-col>
							<van-col span="4">{{item.basics.transmission_name}}|</van-col>
							<van-col span="6">准乘{{item.basics.capacity}}人</van-col>
						</van-row>
					</div>
					<div class="days">
						你的订单时长为{{$route.params.days}}天
					</div>
					<br>
				</div>
				<div class="money" v-for="(item,index) in datas[$route.params.index].car_types" v-if="item.id==$route.params.id">
					<van-submit-bar :price="summoney()*item.prices.day" button-text="提交订单" />
				</div>
			</div>
		</div>
	</div>
	<div v-else>
		<div class="order-top">
			<van-nav-bar title="订车" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="show = true" slot="right" alt="">
				<van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay>
			</van-nav-bar>
		</div>
		<h3>请先选择用车时间</h3>

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
			}
		},
		created() {
			// console.log(this.date)
			console.log(beijing)
			this.datas = beijing.recommends
			console.log(this.datas)
			console.log(carslist.recommends[0].id)
			console.log(carslist.recommends[0].name)
			console.log(carslist.recommends[0].adress)
			console.log(carslist.recommends[0].car_types)

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
			}

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
