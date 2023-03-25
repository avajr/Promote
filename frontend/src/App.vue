<template>
	<TheNavbar />
	<router-view></router-view>
	<TheFooter />
</template>

<script setup>
	import TheNavbar from "@/components/TheNavbar.vue";
	import TheFooter from "@/components/TheFooter.vue";
</script>

<style>
	#app {
		width: 100%;
		height: max-content;
	}
</style>
