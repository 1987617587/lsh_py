<template>
	<div class="goods">
		<van-nav-bar title="商品列表" left-text="返回" right-text="按钮" left-arrow @click-left="onClickLeft" @click-right="onClickRight" />
		<div v-if="goods">
			<h1>商品列表</h1>

<!-- 			<b>分类id：{{goods.id}}</b>
			<br>
			<b>分类名称：{{goods.name}}</b>
			<!-- <apan v-text="goods.name"></apan>
			<br>
			<ul>
				<li v-for="(item,index) in goods.goods">{{item.name}}</li>
			</ul> -->
			<div class="good" >
				<van-card
				v-for="(item,index) in goods"
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
				goods: null,

			}
		},
		created() {
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
		}
	}
</script>

<style>
</style>
