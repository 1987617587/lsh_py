<template>
	<div class="mine">
		<div class="login" style="height: 150px;align-content: center; ">
			<van-button @click="gotologin" round plain type="primary" style=" position: relative;top: 40%; width: 120px;font-size: 20px; height: 30%;"> 登 录 </van-button>
			
		</div>
		<br>
		<div class="mymoney">
			<!-- 左对齐 -->
			<van-row type="flex">
			  <van-col span="6"><h3>我的钱包</h3></van-col>
			  
			</van-row>
			
			<!-- 居中 -->
			<van-row type="flex" justify="center">
			  <van-col span="6"><strong>0元</strong></van-col>
			  <van-col span="6"><strong>0个</strong></van-col>
			  <van-col span="6"><strong>0张</strong></van-col>
			  <van-col span="6"><strong>0分</strong></van-col>
			</van-row>
			<van-row type="flex" justify="center">
			  <van-col span="6">账户余额</van-col>
			  <van-col span="6">悟空币</van-col>
			  <van-col span="6">优惠劵</van-col>
			  <van-col span="6">可用积分</van-col>

			</van-row>
		</div>
		<br>
		<div>
			<!-- 加跳转 to="index"  -->
			<van-cell-group >
				<van-cell center style="height: 60px;font-size: 16px;" value="实名认证"  size=large is-link  to="/login" />
				<van-cell center style="height: 60px;font-size: 16px;"  value="常见问题"   is-link/>
				<van-cell center style="height: 60px;font-size: 16px;" value="意见反馈"   is-link  to="/feedback" />
				<van-cell @click="gotomore" center style="height: 60px;font-size: 16px;" value="更多"   is-link/>
			</van-cell-group>
			
			
			
		</div>
		
	</div>
</template>

<script>
	
	export default{
		methods:{
			gotologin(){
				this.$router.push("/login")
			},
			gotomore(){
				this.$router.push("/more")
			}
			
		}
	}
</script>

<style>
</style>
