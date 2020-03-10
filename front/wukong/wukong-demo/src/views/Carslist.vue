<template>

	<div class="carslist">
		<div class="carslist-top">
			<van-nav-bar title="选车列表" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="gotomore" slot="right" alt="">
				<!-- <van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay> -->
				<van-overlay :show="show" @click="show= false">
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
			</van-nav-bar>



			<div class="time-address" style="display: flex; justify-content: space-between;">
				<div class="time" style="width: 60%; display: flex;">
					<van-cell title="取还时间" :value="date" @click="showtime = true" />

					<van-calendar v-model="showtime" type="range" @confirm="onConfirm" />
					<van-icon name="arrow" />

					<!-- <van-datetime-picker v-model="currentDate" type="datetime" :min-date="minDate" :max-date="maxDate" /> -->
				</div>
				<div @click="gotomap" class="address" style="width: 30%;display: flex; justify-content: space-between;">
					<p style="margin: 0;padding: 0;">选择地址</p>
					<van-icon name="arrow" />
				</div>
			</div>
			<br>
			<div class="carslit-msg" v-for="(items,index) in datas" style="width: 100%;background-color: white;">
				<div class="first" style="width: 96%; margin: 2%; background-color: rgb(253,238,227);">
					<br>
					<van-row>
						<van-col span="16">{{items.name}}</van-col>
						<van-col span="4" offset="2">1.0km</van-col>
					</van-row>
					<br>
					<!-- 评星展示 -->
					<van-row type="flex">
						<van-col span="12" offset="3">
							<div class="start" style="text-align: left;">
								<img style="width: 10%; margin-left:12px ;" src="img/start.png" alt="">
								<img style="width: 10%;" src="img/start.png" alt="">
								<img style="width: 10%;" src="img/start.png" alt="">
								<img style="width: 10%;" src="img/start.png" alt="">
								<img style="width: 10%;" src="img/start.png" alt="">
								<!-- <p>{{items.charging_pile}}</p> -->
							</div>
						</van-col>

					</van-row>
					<p style="text-align: left; padding-left:46px ;">{{items.address}}</p>
					<!-- {{datas[index].address}} -->
					<br>



				</div>
				<!-- {{index}} -->
				<div @click="gotocar(items.id,item.id,days)" class="choose-car" v-for="(item,index1) in cars " style="background-color: white;">
					<div v-if="item.shop == items.id" class="car">
						<van-row type="flex">
							<van-col span="8">
								<img style="width: 100%;" v-if="item.imgs" :src="item.imgs[0].img" alt="">

							</van-col>
							<van-col span="16">
								<van-row type="flex" justify>
									<van-col span="18">
										{{item.name}}
									</van-col>

								</van-row>
								<van-row type="flex">
									<van-col span="12">
										<br>
										<br>
										<strong v-for="(price,index2) in prices" v-if="item.price==price.id" style=" font-size: 20px;color: red;">{{price.avg}}</strong>元/日均价
										<!-- {{item.id}} -->
									</van-col>
									<van-col span="6">
										<!-- {{item.prices.avg}}元/日均价 -->
									</van-col>
									<van-col span="4">
										<van-button @click="gotuOrder(userinfo.id,item.id,days)" round type="info">订</van-button>
									</van-col>

								</van-row>
							</van-col>
						</van-row>
					</div>
					<!-- 					<div v-else>
						{{items.id}}
						<br>
						{{item.shop}}
					</div> -->


					<!-- <img :src=item.pics.pic1 alt="">
					<p>{{item.car_type_name}}</p>
					<p>{{item.prices.avg}}元/日均价</p> -->
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
				showtime: false,
				goodnums: 1,
				date: null,
				cars: null,
				prices: null,
				minDate: new Date(2020, 0, 1),
				maxDate: new Date(2025, 10, 1),
				currentDate: new Date(),
				days: null,
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
			this.onconfirm()

			this.$api.getshops({

			}).then(res => {
				console.log("得到门店列表", res)
				this.datas = res.data
			}).catch(err => {
				console.log("出错了", err)
			})
			this.$api.getcars().then(res => {
				console.log("得到汽车列表", res)
				this.cars = res.data
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
			timeTransform(str) {
				// var str = "2010-08-01";
				// 转换日期格式
				str = str.replace(/-/g, '/'); // "2010/08/01";
				// 创建日期对象
				var datetime = new Date(str);
				// 加一天
				// date.setDate(date.getDate() + 1);
				return datetime
			},
			gotomap() {
				this.$router.push("/map")
			},
			gotomore() {
				this.$router.push("/more")
			},
			gotuOrder(user_id, car_id, days) {
				console.log(user_id,typeof(user_id), car_id,typeof(car_id), days,typeof(days))
				if (this.days) {
					// 创建订单
					this.$api.crerteOrder({
						user: user_id,
						cars: [car_id],
						days: days
					}).then(res => {
						console.log("订单信息", res);
						
						// 跳转订单页面
						this.$router.push("/order")

					}).catch(err => {
						console.log("发生错误", err);
					})

				} else {
					this.$toast('请先选择用车时间');
					// this.$router.push("/carslist")
				}
			},
			gotocar(shop_id, car_id, days) {
				console.log(shop_id, car_id, days)
				if (this.days) {
					this.$router.push("/detail/" + shop_id + "/" + car_id + "/" + days)
				} else {
					this.$toast('请先选择用车时间');
					// this.$router.push("/carslist")
				}
			},
			formatDate(date) {
				return `${date.getMonth() + 1}/${date.getDate()}`;
			},
			onconfirm(date) {
				console.log(this.$route.params.dateto)
				console.log(this.$route.params.dateend)

				this.date = [this.timeTransform(this.$route.params.dateto), this.timeTransform(this.$route.params.dateend)]
				console.log(this.date)

				const [start, end] = this.date;
				console.log("之前拿到的时间", start)
				this.showtime = false;
				this.date = `${this.formatDate(start)} - ${this.formatDate(end)}`;
				console.log(this.date)
				console.log((end - start) / (3600 * 24 * 1000))
				this.days = (end - start) / (3600 * 24 * 1000)
			}

			,
			onConfirm(date) {

				const [start, end] = date;
				console.log('之后拿到的时间', start)
				this.showtime = false;
				this.date = `${this.formatDate(start)} - ${this.formatDate(end)}`;
				console.log(this.date)
				console.log((end - start) / (3600 * 24 * 1000))
				this.days = (end - start) / (3600 * 24 * 1000)


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

		},
		filters: {
			gatavgprice(date) {
				console.log("过滤", date.avg)
				// data = new data.avg
				// return data
				// avgprice = date.avg 
			}
		}


	}
</script>

<style>
	.time .van-cell {
		margin: 0;
		padding: 0;
	}

	/* .block {
		top: 48px;
		right: 16px;
		border-radius: 8%;
		position: absolute;
		width: 160px;
		height: 160px;
		background-color: #fff;
		z-index: 10
	} */
</style>
