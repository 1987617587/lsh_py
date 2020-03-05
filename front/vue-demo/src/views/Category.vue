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
				<li v-for="(item,index) in category.goods">{{item.name}}</li>
			</ul>

		</div>

	</div>
</template>

<script>
	export default {
		data() {
			return {
				category: null,

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
