<template>
	<div class="as">
		
	<h1 @click="mounted()">This is an about page</h1>
	</div>
	
</template>
<script>
	export default {
		data() {
			return {
				show: false
			};
		},

		methods: {
			mounted() {
				this.$dialog.alert({
					message: '请在微信浏览器内打开！'
				});
			}
		}

	}
</script>

<style>
</style>
