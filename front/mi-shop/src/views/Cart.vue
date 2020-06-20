<template>
  <div class="cart">
	  <van-nav-bar class="header"
	    title="购物车"
	    left-arrow
	    @click-left="onClickLeft"
	    @click-right="onClickRight"
	  >
	   <van-icon name="search" slot="right" />
	  </van-nav-bar>
	  
	  <van-cell title="登录后享受更多优惠" is-link value="去登录" to="/mine"/>
	  
	  <div>
		 <van-card v-for="(item,index) in $store.getters.getGoodList"
		   :num="item.num"
		   
		  
		   :title="item.id"
		   thumb="https://img.yzcdn.cn/vant/t-thirt.jpg"
		 > 
		 <van-stepper @change="change(index,item.num)" v-model="item.num" slot="bottom" />
		 
		 </van-card>
		  
	  </div>
	  
  </div>
</template>
<script>
	export	default{
		data(){
			return{
			
			}
		},
		methods:{
			change(index,num){
				console.log(num,index);
				this.$store.commit("changeGoodNUm",[index,num]);
				
			},
			onClickLeft() {
			  // this.$toast('返回');
						this.$router.go(-1);
						
			},
			onClickRight() {
			  // this.$toast('按钮');
						this.$router.push("/search")
			}
		}
	}
	
</script>


<style scoped="scoped" lang="less">

</style>


