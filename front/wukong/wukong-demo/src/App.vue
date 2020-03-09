<template>
	<div id="app">
		<div  id="nav">


			<van-tabbar v-model="active" v-show="$route.meta.tabbar">
				<van-tabbar-item router-link to="/"> 
				<img v-if="active==0" src="img/home.png" slot="icon" alt=""> 
				<img v-else src="img/home-o.png" slot="icon" alt="">首页</van-tabbar-item>
				<van-tabbar-item  router-link to="/service">
				<img v-if="active==1" src="img/myservice.png" slot="icon" alt="">
				<img v-else src="img/service-o.png" slot="icon" alt="">客服</van-tabbar-item>
				<van-tabbar-item  router-link to="/indent">
					<img v-if="active==2" src="img/myident.png" slot="icon" alt="">
					<img v-else src="img/indent-o.png" slot="icon" alt="">订单</van-tabbar-item>
				
				<!-- <van-tabbar-item icon="todo-list" router-link to="/login">订单</van-tabbar-item> -->
				<van-tabbar-item router-link to="/mine">
					<img v-if="active==3" src="img/mine.png" slot="icon" alt="">
					<img v-else src="img/mine-o.png" slot="icon" alt="">我的</van-tabbar-item>
				
			</van-tabbar>

		</div>
		<router-view />
	</div>
</template>
<script>
	export default {
		data() {
			return {
				active: 0
			}
		}
	}
</script>

<style lang="less">
	.van-tabbar-item--active{
		color: red;
	}
</style>

<style lang="less">
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	#nav {
		padding: 0px;

		a {
			font-weight: bold;
			color: #2c3e50;

			&.router-link-exact-active {
				color: #42b983;
			}
		}
	}
	.van-tabbar-item--active {
	    color: red;
	}
</style>
