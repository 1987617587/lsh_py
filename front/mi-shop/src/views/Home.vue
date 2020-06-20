<template>
  <div class="home" v-if="datas">
   <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	 <div class="header">
		 <div class="left">
			 <img src="img/logo.png" alt="">
		 </div>
		 <div class="middle" @click="goToSearch">
			 <van-search :disabled="true" placeholder="请输入搜索关键词" v-model="searchValue" />
		 </div>
		 <div class="right">
			 <img src="img/me.png" alt="">
		 </div>
	 </div>

	
	
	<div class="tabs">
		<van-tabs>
		  <van-tab v-for="(item,index) in datas.tabs" :title="item.name">
		    <!-- 数据应该再次请求网络 利用参数 {{item.page_type}}  {{item.page_id}} -->
			<HomePage :item="item"></HomePage>
		  </van-tab>
		</van-tabs>
	</div>
	
  </div>
</template>
<style scoped="scoped" lang="less">
	.header{
		display: flex;
		line-height: 44px;
		height: 44px;
		.left{
			margin: 0 10px;
			img{
				height: 22px;
				vertical-align: middle;
			}
		}
		.middle{
			flex: 1;
			.van-search{
				padding-top:5px ;
			}
		}
		.right{
			margin: 0 10px;
			img{
				height: 26px;
				vertical-align: middle;
			}
		}
	}
	
</style>


<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import HomePage from '@/components/HomePage.vue'

export default {

  name: 'home',
  components: {
    // HelloWorld
	HomePage
  },
  data(){
	  return{
		  datas:null,
		  searchValue:""
	  }
  },
  created() {
  	this.$http({
		url:"http://biger.applinzi.com/page.php",
		method:"get"
	}).then(res=>{
		// console.log(res.data);
		if(res.data.code==0){
			this.datas = res.data.data;
		}
	})
	
  },
  methods:{
	  goToSearch(){
		  this.$router.push("/search");
	  }
  }
}
</script>
