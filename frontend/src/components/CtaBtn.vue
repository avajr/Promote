<template>
	<div class="cta">
		<router-link :to="props.link">{{ props.cta }}</router-link>
	</div>
</template>

<script setup>
	const props = defineProps({ cta: String, link: String });
</script>

<style lang="css" scoped>
	.cta {
		display: inline-block;
	}
	.cta a:hover {
		background-color: transparent;
		color: var(--secondary-dark);
	}
	.cta a {
		display: inline-block;
		background-color: var(--secondary-dark);
		border: 2px solid var(--secondary-dark);
		border-radius: 8px;
		padding: 0 calc(var(--h6-text) * 1.5);
		text-decoration: none;
		font-weight: 600;
		width: 100%;
		height: max-content;
		line-height: 270%;
		color: var(--secondary-light);
		letter-spacing: 1px;
		font-size: var(--h6-text);
	}
</style>
