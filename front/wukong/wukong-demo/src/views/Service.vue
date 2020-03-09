<template>
	<div class="service">
		<div class="service-top">
			<van-row>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;border-right: none;">
						<br>
						<br>
						<img style="width: 30%; " src="img/car.png" alt="">
						<p style="margin: 10px;">取还车辆</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid; border-top: none;border-right: none;">
						<br>
						<br>
						<img style="width: 30%; " src="img/money.png" alt="">
						<p style="margin: 10px;">计费规则</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;">
						<br>
						<br>
						<img style="width: 30%; " src="img/money2.png" alt="">
						<p style="margin: 10px;">费用明细</p>
						<br>
					</div>
				</van-col>
			</van-row>
		</div>

		<div class="service-mid">
			<van-row>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;border-right: none;">
						<br>
						<p>注册会员</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid; border-top: none;border-right: none;">
						<br>
						<p>认证审核</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;">
						<br>
						<p>订单支付</p>
						<br>
					</div>
				</van-col>
			</van-row>
			<van-row>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;border-right: none;">
						<br>
						<p>订单修改</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid; border-top: none;border-right: none;">
						<br>
						<p>预定车辆</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;">
						<br>
						<p>违章处理</p>
						<br>
					</div>
				</van-col>
			</van-row>
			<van-row>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;border-right: none;">
						<br>
						<p>出险理赔</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid; border-top: none;border-right: none;">
						<br>
						<p>退款说明</p>
						<br>
					</div>
				</van-col>
				<van-col span="8">
					<div class="top1" style="border: 1px rgb(240,240,240) solid;border-top: none;">
						<br>
						<p>其他问题</p>
						<br>
					</div>
				</van-col>
			</van-row>
		</div>

		<div class="service-end">
			<div @click="gotoonline" class="end1">
				<br>
				<br>
				<van-row>
					<van-col span="4"><img src="img/service.png" alt="" style="width:60%"></van-col>
					<van-col span="16">
						<div class="msg">
							<van-row type="flex" style="font-size:16px;font-weight: 600;">
								<van-col span="7">
									<p>在线客服</p>
								</van-col>
							</van-row>
							<van-row type="flex" style="font-size: 14px;font-weight: 300;">
								<van-col span="17">
									<p>人工客服在线解答您的疑惑</p>
								</van-col>
							</van-row>
						</div>
					</van-col>
					<van-col span="4">
						<van-cell title="" is-link />
					</van-col>
				</van-row>
			</div>
			<br>
			<div @click="gotophone" class="end2" style="border-top:1px rgb(240,240,240) solid;">
				<br>
				<van-row>
					<van-col span="4"><img src="img/phonehot.png" alt="" style="width:60%"></van-col>
					<van-col span="16">
						<div class="msg">
							<van-row type="flex" style="font-size:16px;font-weight: 600;">
								<van-col span="7">
									<p>电话热线</p>
								</van-col>
							</van-row>
							<van-row type="flex" style="font-size: 14px;font-weight: 300;">
								<van-col span="24">
									<p>24小时服务热线为您服务 400-0515-507</p>
								</van-col>
							</van-row>
						</div>
					</van-col>
					<van-col span="4">
						<van-cell title="" is-link />
					</van-col>
				</van-row>
			</div>

			<!-- <van-overlay :show="show1" @click="show = false" /> -->
			<van-overlay :show="show1" @click="show = false">
				<div class="wrapper" @click.stop>
					<div class="block" >
						<br>
						<h3>拨打电话</h3>
						<p  class="msgbox-message">要打给人工客服400-0515-507吗？</p>
						<div data-v-ce71e002="" style="display: flex; justify-content:space-between; margin: 10px; " >
							<!-- <button data-v-ce71e002="" type="button" name="button" class="msgbox-cancel">先不打</button> -->
							<van-button @click="gotophone" size="small"  type="info">先不打</van-button>
							<van-button @click="fail" size="small" type="danger">立即拨打</van-button>
							<!-- <button data-v-ce71e002="" type="button" name="button" class="msgbox-confirm">立即拨打</button> -->
						</div>
					</div>
				</div>
			</van-overlay>


		</div>

	</div>

	</div>
</template>

<script>
	export default {

		data() {
			return {
				show1: false,
			}
		},
		methods: {
			gotoonline() {
				window.location.href = "https://wkzuche.udesk.cn/im_client/?web_plugin_id=62123"
			},
			gotophone() {
				this.show1 = !this.show1
			},
			fail(){
				this.$toast('请在手机端拨打');
			}


		}
	}
</script>

<style scoped="scoped" lang="less">
	p {
		margin: 0;
		padding: 0;
	}

	.service-mid p {
		margin: 10px;
	}

	.wrapper {
		position: absolute;
		top: 200px;left: 280px;
		display: flex;
		align-items: center;
		justify-content: center;
		height: 100%;
	}

	.block {
		width: 160px;
		height: 160px;
		background-color: #fff;
		border-radius: 5%;
	}
</style>
