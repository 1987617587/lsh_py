<template>
  <div class="mine">
    <div class="header">
		<van-nav-bar
		  id="searchdiv"
		  title="标题"
		  
		 
		  left-arrow
		  @click-left="onClickLeft"
		  @click-right="onClickRight"
		>
		
		<input v-model="value" id="searchinput" slot="title" placeholder="请输入搜索内容" />
		
		<van-icon name="search" slot="right" />
		</van-nav-bar>
	</div>
	
	<div class="other">
		<p>历史搜索</p>
		<div class="searchhot">
			<van-tag class='searchitem' @click="searchHot(item)" v-for="item in searchHistory" :type="colors[ parseInt(Math.random()*colors.length)  ]">{{item}}</van-tag>
			
		</div>
		
		<p>热门搜索</p>
		<img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/0087312fb580d3b571178fbcb6b27f89.jpg?w=1080&h=300&bg=E2E6EF" alt="">
		
		<div class="searchhot">
			<van-tag class='searchitem' @click="searchHot(item)" v-for="item in 19" :type="colors[ parseInt(Math.random()*colors.length)  ]">搜索{{item}}</van-tag>
			
		</div>
		
		
	
	</div>
  </div>
</template>
<style scoped="scoped" lang="less">
	.header{
		
		#searchdiv{
			background-color: #f2f2f2;
		}
		#searchinput{
			height: 30px;
			line-height: 30px;
			border: none;
		}
	}
	.other{
		img{
			width: 100%;
		}
		.searchhot{
			padding: 20px;
			display: flex;
			flex-wrap: wrap;
			.searchitem{
				margin: 10px;
				padding: 10px;
			}
		}
	}
</style>
<script>
	export default {
		data(){
			return{
				value:"",
				colors:["primary","success","danger","warning"],
				historySearch: JSON.parse(localStorage.getItem("historySearch"))||[]
			}
		},
		computed:{
			searchHistory(){
				return this.historySearch
			}
		},
	  methods: {
	    onClickLeft() {
		  this.$router.go(-1)
	    },
	    onClickRight() {
			if(this.value.length<=0){
				this.$toast("请输入搜索内容")
			}
			else{
				this.historySearch.unshift(this.value);
				localStorage.setItem("historySearch",JSON.stringify(this.historySearch))
			}
	    },
		searchHot(item){
			this.$toast(`搜索了${item}`);
		}
	  }
	}
</script>