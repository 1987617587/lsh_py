import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	// data
  state: {
	  goodList:[],
	  // [{id:101,num:20},{id:102,num:1}]
  },
  // computed
  getters:{
	  getGoodList(state){
		  return state.goodList
	  }
  },
  // methods
  mutations: {
	  addGood(state,good){
		  // state.goodList.push(good);
		  let canAdd=true;
		  let index = -1;
		  state.goodList.forEach((item,i)=>{
			  if(item.id==good.id){
				  canAdd=false;
				  index = i
			  }
		  })
		  
		  if(canAdd){
			  state.goodList.push(good);
		  }
		  else{
			  state.goodList[index].num+=good.num;
		  }
	  },
	  changeGoodNUm(state,index_num){
		  console.log(index_num[0],index_num[1],"++");
		  state.goodList[index_num[0]].num = index_num[1];
	  }
  },
  // promise
  actions: {
  },
  // 模块
  modules: {
  }
})
