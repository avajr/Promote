<template>
	<div class="value-card">
		<div class="icon-wrapper">
			<img :src="props.icon" alt="" />
		</div>
		<div class="card-content">
			<h5 class="light-text">{{ props.title }}</h5>
			<p class="light-text" style="opacity: 0.8">{{ props.text }}</p>
		</div>
		<div class="bottom-line"></div>
	</div>
</template>

<script setup>
	const props = defineProps({ icon: String, title: String, text: String });
</script>

<style scoped>
	.value-card {
		max-width: 380px;
		width: 100%;
		max-height: 480px;
		height: max-content;
		padding: 50px 40px;
		display: flex;
		flex-direction: column;
		align-items: center;
		background: linear-gradient(180deg, #36363e 0%, #292930 100%);
		border: 1px solid #424249;
		border-radius: 30px;
		margin-bottom: 40px;
	}
	.value-card p {
		height: 112px;
		overflow: hidden;
		word-wrap: break-word;
	}
	.bottom-line {
		width: 80px;
		border: 1px solid #fff;
	}
	.icon-wrapper {
		width: 150px;
		height: 150px;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
		background-color: #292930;
	}
	.icon-wrapper img {
		width: 70%;
	}
	.card-content {
		text-align: center;
		margin: 25px 0px;
		overflow: hidden;
		display: flex;
		flex-direction: column;
		row-gap: 8px;
	}
</style>
