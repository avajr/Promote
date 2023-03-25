<template>
	<div class="cta cta-white">
		<router-link :to="props.link">{{ props.cta }}</router-link>
	</div>
</template>

<script setup>
	const props = defineProps({ cta: String, link: String });
</script>

<style lang="css" scoped>
	.cta-white {
		display: inline-block;
	}
	.cta-white a:hover {
		background-color: transparent;
		color: var(--secondary-light);
	}
	.cta-white a {
		display: inline-block;
		background-color: var(--secondary-light);
		border: 2px solid var(--secondary-light);
		border-radius: 8px;
		padding: 0 calc(var(--h6-text) * 1.5);
		text-decoration: none;
		font-weight: 600;
		width: 100%;
		height: max-content;
		line-height: 270%;
		color: var(--secondary-dark);
		letter-spacing: 1px;
		font-size: var(--h6-text);
	}
</style>
