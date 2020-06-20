<template>
  <div id="app">
    
    <router-view/>
	
	
	<!-- <div id="nav">
	  <router-link to="/">首页</router-link> |
	  <router-link to="/category">分类</router-link> |
	  <router-link to="/detail/101">详情</router-link> |
	  <router-link to="/search">搜索</router-link> |
	  <router-link to="/cart">购物车</router-link> |
	  <router-link to="/mine">我的</router-link> 
	</div> -->
	
	<van-tabbar v-show="$route.meta.tabbar" active-color="#ff6700" route v-model="active">
	  <van-tabbar-item icon="home-o" to="/">首页</van-tabbar-item>
	  <van-tabbar-item icon="description" to="/category">分类</van-tabbar-item>
	  <van-tabbar-item icon="cart-o" to="/cart">购物车</van-tabbar-item>
	  <van-tabbar-item icon="friends-o" to="/mine">我的</van-tabbar-item>
	</van-tabbar>
	
	
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
  a{
	  font-weight: bold;
	  // color: #2c3e50;
	  text-decoration: none;
	  &.router-link-exact-active{
		  color: #42b983;
	  }
  }
}


</style>
