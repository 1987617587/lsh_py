<template>
  <div class="search" v-if="datas">
    <div @click="$router.go(-1)" class="return" style="border-radius: 50%; z-index: 100; background-color: rgba(0,0,0,0.6); position: absolute;left: 20px;top: 20px; width: 32px;height: 32px;">
		<img src="img/return.png" alt="" style="width: 100%;">
	</div>
	
	<van-swipe :autoplay="3000" indicator-color="white">
	  <van-swipe-item v-for="(item,index) in datas.goods_info[0].gallery_v3">
		  <img :src="item.img_url" alt="" style="width: 100%;">
	  </van-swipe-item>
	 
	</van-swipe>
	
	<p >{{datas.product_info.name}}</p>
	
	<p @click="show=true">选择配置参数</p>
	<van-popup v-model="show" position="bottom" :style="{ height: '80%' }">
		<div>
			选择购买个数：<van-stepper v-model="buyNum" />
		</div>
		
		<van-button type="primary" @click="addCart">加入购物车</van-button>
	</van-popup>
	
	<van-goods-action>
	  <van-goods-action-icon icon="chat-o" text="首页" @click="goToHome" />
	  <van-goods-action-icon icon="cart-o" @click="$router.push('/cart')" text="购物车" :info="$store.getters.getGoodList.length" />
	  <van-goods-action-icon icon="shop-o" text="客服" info="12" />
	  <van-goods-action-button type="warning" text="加入购物车" @click="show=true" />
	</van-goods-action>
  </div>
</template>

<script>
	export default{
		data(){
			return{
				datas:null,
				show:false,
				buyNum:1
			}
		},
		methods:{
			goToHome(){
				this.$router.push("/")
			},
			addCart(){
				this.show=false;
				
				this.$toast("加入成功")
				this.$store.commit("addGood",{id:this.$route.params.id,num: this.buyNum} )
			}
		},
		created() {
			this.$http({
				url:`http://biger.applinzi.com/product.php?id=${this.$route.params.id}`,
				method:"get"
			}).then(res=>{
				if(res.data.code==0)
				{
					console.log(res.data.data);
					this.datas=res.data.data;
				}
				
			})
		}
	}
	
	
</script>
