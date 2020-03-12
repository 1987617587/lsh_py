<template>

	<div class="carslist">
		<div class="carslist-top">
			<van-nav-bar title="筛选信息列表" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
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







		</div>
		<van-search v-model="value" 
		placeholder="请输入搜索关键词"
		 show-action
		 use-left-icon-slot
		   ><van-icon @click="gotosearch" slot="left-icon" name="search" />
			   </van-search>
		
		
		
			<!-- <van-search
			label="品牌"
			  value="value"
			  placeholder="请输入搜索关键词"
			  @click="gotosearch"
			>
			</van-search> -->
			
			<!-- 历史搜索 -->
			<van-row >
				
			  <van-col v-for="(category,index) in categories" span="3">
				  <van-tag round type="primary">标签</van-tag>
			</van-col>
		
			</van-row>
					
			<br>	
			<br>	
			<!-- 分类标签展示 -->
			<van-row >
				
			  <van-col v-for="(category,index) in categories" span="4">
				  <van-button @click="gotosearchcategory(category.name)" size="mini" :color="colors[parseInt(Math.random()*colors.length)]">{{category.name}}</van-button>
			</van-col>
		
			</van-row>
			
		
	
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
				border:true,
				 show: {
				        primary: true,
				        success: true
				      },
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
				userinfo: null,
				value: '',
				categories:null,
				colors:[
					"#7232dd",
					"#728221",
					"#2282dd",
					"#72d32d",
					"linear-gradient(to right, #4bb0ff, #6149f6)",
				]
			}
		},
		created() {
			this.$api.getUserinfo().then(res => {
				console.log("个人信息", res)
				this.userinfo = res.data;
			}).catch(err => {
				console.log("出错了");
			})

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
			// 获取分类标签
			this.getcategories()

		},
		methods: {
			close(type) {
			      this.show[type] = false;
				  },
		onChange(e) {
		    this.setData({
		      value: e.detail
		    });
			console.log("搜索",this.value)
		  },
		
		  onSearch() {
		    this.toast('搜索' + this.data.value);
			console.log("搜索",this.value)
		  },
		
		  onClick() {
		    Toast('搜索' + this.data.value);
		  },
			gotomap() {
				this.$router.push("/map")
			},
			gotomore() {
				this.$router.push("/more")
			},
			gotuOrder(user_id, car_id, days) {
				console.log(user_id, typeof(user_id), car_id, typeof(car_id), days, typeof(days))
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
			// 搜索分类
			gotosearchcategory(category){
				console.log("搜索",category)
				this.$router.push("/searchlist/categories/"+category+"/")
			},
			// 搜索汽车品牌
			gotosearch(){
				console.log("搜索",this.value)
				this.$router.push("/searchlist/cars/"+this.value+"/")
				
			},
			getcategories(){
				this.$api.getCategories({
				}).then(res=>{
					console.log("获取分类成功",res)
					this.categories = res.data
				}).catch(err=>{
					console.log("出错了",err)
				})
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
