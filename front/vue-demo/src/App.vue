<template>
	<div id="app">
		<!--    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
		<router-view />
		
		<van-tabbar route v-model="active">
			<van-tabbar-item to="/"  icon="home-o">首页</van-tabbar-item>
			<van-tabbar-item to="/goods"  icon="search">标签</van-tabbar-item>
			<van-tabbar-item to="/usercenter"  icon="friends-o">我的</van-tabbar-item>
			<van-tabbar-item to="/regist"  icon="setting-o">注册</van-tabbar-item>
		</van-tabbar>
			
	</div>

	
		
</template>
<script>
	export default {
		data() {
			return {
				active: 0
			}
		},

		computed: {
			// 计算属性不能判断cookie变化 但是可以判断 store数据状态管理器数据变化
			islog() {
				return this.$store.getters.getLog
			}
		},
		methods: {

		}

	}
</script>

<style lang="less">
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	#nav {
		padding: 30px;

		a {
			font-weight: bold;
			color: #2c3e50;

			&.router-link-exact-active {
				color: #42b983;
			}
		}
	}
</style>
