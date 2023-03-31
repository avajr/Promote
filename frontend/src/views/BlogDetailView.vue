<template>
	<img id="banner-img" src="@/assets/img/banner.png" alt="" />
	<div class="case-study-detail-page">
		<div class="container" v-for="blog in blogs" :key="blog.id">
			<section>
				<div class="case-study-entry">
					<p class="dark-text">{{ blog.created_at }}</p>
				</div>
				<h1 class="case-study-title">{{ blog.title }}</h1>
				<div class="case-study-cover">
					<img :src="blog.cover_img" alt="" />
				</div>
				<div class="case-study-content">
					<div
						class="case-study-content-inner"
						v-html="blog.content"
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
	let blogs = ref();

	const getBlogs = async (url) => {
		const response = await $axios.get(url);
		blogs.value = [response.data];
		console.log(response.data);
	};

	// Life Cycle
	onMounted(() => {
		getBlogs(`/blogs/${route.params.id}`);
	});
</script>

<style scoped>
	#banner-img {
		position: absolute;
		top: 0;
		left: 0;
		z-index: 0;
		width: 100%;
		height: 600px;
	}

	.case-study-detail-page {
		position: relative;
		padding: 60px 0px;
		z-index: 10;
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
		margin: 40px 0px 160px;
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
	.case-study-content-inner {
		max-width: 900px;
		width: 100%;
		margin: 0 auto;
		padding: 0px 20px;
	}
</style>
