<template>
	<div class="category">
		<van-nav-bar title="分类详情" left-text="返回" right-text="按钮" left-arrow @click-left="onClickLeft" @click-right="onClickRight" />
		<!-- <h1>这是分类{{$route.params.id}}</h1> -->
		<div v-if="category">

			<b>分类id：{{category.id}}</b>
			<br>
			<b>分类名称：{{category.name}}</b>
			<!-- <apan v-text="category.name"></apan> -->
			<br>
			<ul>
				<!-- <li v-for="(item,index) in goods">{{item|categorygoods}}</li> -->
				<!-- <li v-for="(item,index) in goods" v-if="item.category.id == category.id" >{{item.name}}</li> -->
			</ul>
			<div class="good" >
				<van-card
				v-for="(item,index) in goods" v-if="item.category.id == category.id" 
				  num="2"
				  price="2.00"
				  :desc="item.desc"
				  :title="item.name"
				  :thumb="item.images[0].img"
				>
				  <div slot="tags">
				    <van-tag plain type="danger">{{item.category.name}}</van-tag>
				  </div>
				  <div slot="footer">
				    <van-button size="mini">按钮</van-button>
				    <van-button size="mini">按钮</van-button>
				  </div>
				</van-card>
			</div>
			

		</div>

	</div>
</template>

<script>
	export default {
		data() {
			return {
				category: null,
				goods:null,
				

			}
		},
		created() {
			this.$api.getCategoryDetail({
				id: this.$route.params.id
			}).then(res => {
				console.log("分类详情", res);
				this.category = res.data
				
			}).catch(err => {
				console.log("发生错误", err);
			})
			this.$api.getgoods({
				
			}).then(res => {
				console.log("商品列表", res);
				this.goods = res.data
				
			}).catch(err => {
				console.log("发生错误", err);
			})

		},
		methods: {
			onClickLeft() {
				this.$router.go(-1)
			},
			onClickRight() {
				this.$toast('按钮');
			}
		},
		filters:{
			categorygoods(goods){
				if(goods.category.id == this.category.id){
					console.log(goods);
				}
				
				// return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
	}
</script>

<style>
</style>
