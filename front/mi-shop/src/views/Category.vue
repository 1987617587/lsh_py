<template>
  <div class="category" v-if="datas">
    <van-nav-bar class="header"
      title="分类"
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    >
	 <van-icon name="search" slot="right" />
	</van-nav-bar>
	
	<div class="main">
		<div class="left">
			<van-sidebar @change="onChange" v-model="activeKey">
			  <van-sidebar-item v-for="(item,index) in datas" :title="item.category_name" />
			</van-sidebar>
		</div>
		<div class="right" ref="right">
			<div v-for="(item,index) in datas" v-if="index==activeKey">
				<div v-for="(item1,index) in item.category_list">
					
					
						
							<div class="cells_auto_fill" v-if="item1.view_type=='cells_auto_fill'">
								<img :src="item1.body.items[0].img_url" alt="">
							</div>
							<div class="category_title" v-if="item1.view_type=='category_title'">
								<van-divider :style="{ color: '#1989fa', borderColor: '#1989fa', padding: '0 16px' }">
								  {{item1.body.category_name}}
								</van-divider>
							</div>
							<div class="category_group" v-if="item1.view_type=='category_group'">
								
									<div class="item2" v-for="(item2,index) in item1.body.items">
										<router-link :to="'/detail/'+item2.action.path">
											<img :src="item2.img_url" alt="">
											<p>{{item2.product_name}}</p>
										</router-link>
									</div>
								
							</div>
						
						
						
				
					
					
					
					
					
				</div>
			</div>
		</div>
	</div>
	
  </div>
</template>
<style scoped="scoped" lang="less">
	.category{
		.header{
			background-color: rgb(242,242,242);
			line-height: 50px;
			height: 50px;
			
		}
		.main{
			display: flex;
			position: absolute;
			left:0;
			top:50px;
			right:0;
			bottom: 50px;
			.left{
				overflow-y: auto;
				width: 25%;
				.van-sidebar-item--select{
					border:none;
					color: #fb7d34;
					font-size: 16px;
				}
			}
			// webkit内核浏览器控制滚动条不显示
			.left::-webkit-scrollbar{
				display: none;
				
			}
			.right::-webkit-scrollbar{
				display: none;
				
			}
			.right{
				overflow-y: auto;
				width: 75%;
				.cells_auto_fill{
					img{
						width: 100%;
					}
				}
				
				.category_group{
					display: flex;
					flex-wrap: wrap;
					.item2{
						display: flex;
						flex-direction: column;
						width: 87px;
						height: 80px;
						margin: 10px 0 15px;
						align-items: center;
						img{
							width: 52px;
							height: 52px;
						}
						p{
							font-size: 12px;
						}
					}
				}
				
			}
		}
	}
</style>

<script>
	export default{
		methods: {
		  onChange(index) {
			// 在左侧点击时需要控制右侧滚动条位置
			// 通过$refs 找到需要控制的dom元素  控制元素的滚动条到顶部
		    this.$refs.right.scrollTo(0,0);  
		  },
		  onClickLeft() {
		    // this.$toast('返回');
			this.$router.go(-1);
			
		  },
		  onClickRight() {
		    // this.$toast('按钮');
			this.$router.push("/search")
		  }
		},
		data(){
			return{
				datas:null,
				activeKey:0
			}
		},	
		
		created() {
			this.$http({
				url:"http://biger.applinzi.com/category.php",
				method:"get"
			}).then(res=>{
				if(res.data.code==0){
					this.datas=res.data.data;
				}
				
			})
			
		}
		
	}
	
</script>


<!-- 
1,获取分类页面数据 
2,布局页面(header,left,right)
	左侧使用  侧边栏 
	右侧  循环数据获取多个div   通过左侧的activekey控制右侧div的显示
	
		右侧分三种
		 大图
		 标题
		 分组 
			项目（图片 文字）
 
 
 -->