import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	// 相当于vue data
  state: {
	  islog:false,
	  
	  goodList:[]
  },
    // 相当于vue 计算属性compute
  getters:{
	  // data永远等于state 不需要关注
	  getlog(state){
		  return state.islog
	  },
	  
	  getGoodList(data){
		  return data.goodList
	  }
  },
  // 相当于vue methods
  mutations: {
	  // data永远等于state
	  setlog(state,b){
		state.islog = b  
	  },
	  
	  addGood(data,good){
		  // data.goodList.push(good);
		  // 重复商品合并加入
		  let canAdd =true;
		  let index = -1;
		  data.goodList.forEach((item,i)=>{
			  if(item.id == good.id){
				  canAdd = false
				  index = i
			  }
		  })
		  if(canAdd){
			  data.goodList.push(good);
		  }else{
			  data.goodList[index].num+=good.num;
		  }
		  
	  },
	  // item为数组[index,num]
	  changeGoodNum(data,item){
		  data.goodList[item[0]].num = item[1]
	  },
	  delGood(data,index){
		   data.goodList.splice(index,1)
	  },
  },
  // 相当于vue promise
  actions: {
  },
  // 相当于vue 模块化
  modules: {
  }
})