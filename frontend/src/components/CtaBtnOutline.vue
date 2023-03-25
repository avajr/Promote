<template>
	<div class="cta cta-outline">
		<router-link :to="props.link">{{ props.cta }}</router-link>
	</div>
</template>

<script setup>
	const props = defineProps({ cta: String, link: String });
</script>

<style lang="css" scoped>
	.cta-outline {
		display: inline-block;
	}
	.cta-outline a:hover {
		background-color: var(--secondary-dark);
		color: var(--secondary-light);
	}
	.cta-outline a {
		display: inline-block;
		background-color: transparent;
		border: 2px solid var(--secondary-dark);
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
