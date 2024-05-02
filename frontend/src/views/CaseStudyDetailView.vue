<template>
	<div class="case-study-detail-page">
		<div
			class="container"
			v-for="caseStudy in caseStudies"
			:key="caseStudy.id"
		>
			<section>
				<div class="case-study-entry">
					<img :src="caseStudy.company_logo" alt="" />
					<div></div>
					<p class="dark-text">{{ caseStudy.created_at }}</p>
				</div>
				<h1 class="case-study-title">{{ caseStudy.title }}</h1>
				<div class="case-study-cover">
					<img :src="caseStudy.cover_img" alt="" />
				</div>
				<div class="case-study-details">
					<div>
						<h5>Client</h5>
						<p>{{ caseStudy.client }}</p>
					</div>
					<div>
						<h5>Service</h5>
						<p>{{ caseStudy.service.title }}</p>
					</div>
					<div>
						<h5>Platform</h5>
						<p>{{ caseStudy.platform }}</p>
					</div>
				</div>
				<hr />
				<div class="case-study-content">
					<div
						class="case-study-content-inner"
						v-html="caseStudy.content"
					></div>
				</div>
			</section>
		</div>
	</div>
</template>

<script setup>
	import { useRoute } from "vue-router";
	import { $axios } from "@/plugins/axios";
	import { onMounted, reactive, ref, computed } from "vue";

	const route = useRoute();
	let caseStudies = ref();

	const getCaseStudies = async (url) => {
		const response = await $axios.get(url);
		caseStudies.value = [response.data];
		console.log(response.data);
	};

	// Life Cycle
	onMounted(() => {
		getCaseStudies(`/case-studies/${route.params.id}`);
	});
</script>

<style scoped>
	.case-study-detail-page {
		padding: 60px 0px;
	}
	.case-study-entry {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.case-study-entry div {
		width: 15px;
		border: 2px solid var(--primary-blue);
		border-radius: 40px;
		margin: 0px 20px;
	}
	.case-study-entry p {
		font-size: 1.275rem;
	}
	.case-study-title {
		margin: 20px 0px 0px 0px;
		text-align: center;
		font-weight: 700;
	}
	.case-study-cover {
		width: 100%;
		margin: 40px 0px;
		overflow: hidden;
	}
	.case-study-cover img {
		width: 100%;
		border-radius: 30px;
		object-fit: contain;
	}
	.case-study-details {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-evenly;
		align-items: center;
	}
	hr {
		margin: 60px 0px 90px 0px;
	}
	.case-study-content-inner {
		max-width: 900px;
		width: 100%;
		margin: 0 auto;
	}
</style>
