<template>

	<div class="feedback">
		<div class="feedback-top">
			<van-nav-bar title="意见反馈" left-arrow @click-left="onClickLeft" @click-right="onClickRight">
				<img style="width: 25px;height: 10px;" src="img/more.png" @click="show = true" slot="right" alt="">
				<van-overlay :show="show" @click="show = false">
					<div class="wrapper">
						<div class="block" />
					</div>
				</van-overlay>
			</van-nav-bar>



		</div>



		<div class="feedback-body">
			<div class="feedback-msg">
				<van-cell-group>
					<van-field v-model="message" rows="2" autosize label="意见反馈:" type="textarea" maxlength="200ss" placeholder="请输入意见"
					 show-word-limit />
				</van-cell-group>

			</div>
			<p style="text-align: right; font-size: 12px; padding:0 10px 10px 0;">最多还可以输入{{200-message.length}}字</p>
			<van-button @click="submission" type="primary" size="large">提交</van-button>



		</div>
		<div class="comment">
			<van-divider contentPosition="center" customStyle="color: #1989fa;border-color: #1989fa;font-size: 18px;">用户评论</van-divider>
		
			<div v-for="(comment,index) in comments">
				<van-notice-bar
			  :text="comment.create_time +'用户昵称：'+comment.name+'发表了言论--'+comment.body"
			  left-icon="//img.yzcdn.cn/public_files/2017/8/10/6af5b7168eed548100d9041f07b7c616.png"
			/>
			</div>	
		
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				show: false,
				message: "",
				comments:null,
				userinfo:null,
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log("个人信息",res)
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("出错了");
			})
			this.$api.getComments().then(res=>{
				console.log("获得评论信息",res)
				this.comments = res.data
			}).catch(err=>{
				console.log("出错了")
			})
		},
		methods: {
			onClickLeft() {
				// this.$toast('返回');
				this.$router.go(-1)
			},
			onClickRight() {
				// this.$toast('按钮');
			},
			gotoservice() {
				this.$router.push("/service")
			},
			gotoindent() {
				this.$router.push("/indent")
			},
			gotohome() {
				this.$router.push("/")
			},
			gotojuan() {
				this.$router.push("/service")
			},
			togoAgreement() {
				this.$router.push("/agreement")
			},
			togocall() {
				this.$router.push("/call")
			},
			submission() {
				if (this.message) {
					this.$api.comment({
						name:this.userinfo.username,
						body:this.message,
						user:this.userinfo.id
					}).then(res=>{
						this.$toast('提交成功');
					this.message = ""
					this.$router.go(0)
					
					}).catch(err=>{
						this.$toast('提交失败')
					})
					
					
				} else {
					this.$toast('请先输入');
				}

			}

		}
	}
</script>
<style lang="less">
	.feedback-msg {
		.van-field__word-limit {
			display: none;
		}
	}
</style>


<style scoped="scoped" lang="less">
	* {
		margin: 0;
		padding: 0;
	}

	.van-field__word-limit {
		width: 10px;
		height: 10px;
		background-color: red;
	}

	.van-button--large {
		width: 94%;
		height: 40px;
		line-height: 38px;
	}

	.feedback-body {
		width: 100%;
		// height: 500px;
		// background-color: red;
	}

	.feedback-msg {
		padding: 2%;
		width: 96%;
		// background-color: wheat;
	}

	.block {
		top: 48px;
		right: 16px;
		border-radius: 8%;
		position: absolute;
		width: 160px;
		height: 160px;
		background-color: #fff;
		z-index: 10
	}

	.van-nav-bar {
		width: 100%;
		height: 46px;
		color: red;
		z-index: 10;
	}

	.van-hairline--bottom {
		width: 100%;
		height: 46px;
		color: red;
		z-index: 10;
	}

	h4 {
		margin: 0;
		padding: 0;
		font-size: 20px;
		font-weight: 500;
	}
</style>
