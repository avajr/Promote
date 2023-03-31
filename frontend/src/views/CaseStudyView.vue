<template>
	<div id="case-study-page">
		<header
			class="case-study-header"
			:style="{ 'background-image': 'url(' + banner_bg + ')' }"
		>
			<h1 class="display-text">
				Case <span class="blue-text">Study</span>
			</h1>
		</header>
		<section id="case-studies">
			<div class="container">
				<div class="section__header">
					<img src="@/assets/img/icons/sections/copy.svg" alt="" />
					<div class="section__titles">
						<p class="" style="opacity: 0.8">
							<span class="gold-text">//</span> CASE STUDIES
						</p>
						<h2 class="">Browse our case studies</h2>
					</div>
				</div>
				<div class="case-studies-list">
					<ul>
						<li
							class="card"
							v-for="caseStudy in paginatedData"
							:key="caseStudy.id"
						>
							<div class="card-img">
								<img :src="caseStudy.cover_img" alt="" />
							</div>
							<div class="card-content">
								<div class="company_logo">
									<img :src="caseStudy.company_logo" alt="" />
								</div>
								<hr />
								<h5 style="font-weight: 600">
									{{ caseStudy.title }}
								</h5>
								<p>{{ caseStudy.short_description }}</p>
								<router-link
									class="btn"
									:to="`/case-study/${caseStudy.id}`"
									>Read Case Study</router-link
								>
							</div>
						</li>
					</ul>
					<div class="pagination-btns">
						<button
							@click="previousPage"
							:disabled="currentPage === 1"
						>
							&lt; Previous
						</button>
						<button
							@click="nextPage"
							:disabled="currentPage === totalPages"
						>
							Next &gt;
						</button>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup>
	import banner_bg from "@/assets/img/about/about-banner.png";
	import { $axios } from "@/plugins/axios";
	import { onMounted, reactive, ref, computed } from "vue";

	let caseStudies = ref();

	const data = ref([]);

	const itemsPerPage = 1;
	const currentPage = ref(1);

	const paginatedData = computed(() => {
		const startIndex = (currentPage.value - 1) * itemsPerPage;
		const endIndex = startIndex + itemsPerPage;
		return data.value.slice(startIndex, endIndex);
	});

	const totalPages = computed(() =>
		Math.ceil(data.value.length / itemsPerPage)
	);

	function nextPage() {
		currentPage.value += 1;
	}

	function previousPage() {
		currentPage.value -= 1;
	}

	const getCaseStudies = async (url) => {
		const response = await $axios.get(url);
		caseStudies.value = response.data;
		data.value = response.data;
		console.log(response.data);
	};

	// Life Cycle
	onMounted(() => {
		getCaseStudies("/case-studies/");
	});
</script>

<style scoped>
	#case-study-page {
		width: 100%;
	}
	.case-study-header {
		width: 100%;
		height: 60vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-repeat: no-repeat;
		background-position: center top;
	}

	#case-study-page .section__header {
		flex-direction: column;
		row-gap: 24px;
		text-align: center;
	}

	.card {
		min-height: 560px;
		list-style: none;
		display: grid;
		grid-template-columns: 1fr 1fr;
		column-gap: 50px;
		width: 100%;
		padding: 50px;
		background: linear-gradient(
			124.11deg,
			#e9f7ff 5.58%,
			#ffdbd5 21.8%,
			#fff3ca 37.36%
		);
		border-radius: 10px;
		margin: 25px 0px;
	}
	.card-img {
		width: 100%;
		height: 100%;
	}
	.card-img img {
		border-radius: 10px;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}
	.card-content {
		border-radius: 10px;
		background-color: #fff;
		padding: 50px 40px;
	}
	hr {
		margin: 20px 0px;
	}
	.card p {
		margin: 10px 0px 40px 0px;
	}
	.btn {
		text-decoration: none;
		color: #fff;
		background: var(--secondary-dark);
		padding: 18px 30px;
		border-radius: 8px;
	}
	.btn:hover {
		color: #fff;
		background: var(--secondary-gray);
	}

	.pagination-btns {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-top: 40px;
	}
	.pagination-btns button {
		background: transparent;
		border: none;
		font-size: 1.5rem;
		font-weight: 00;
		cursor: pointer;
	}
	.pagination-btns button:hover {
		color: var(--primary-blue);
	}

	/* MEDIA */
	@media screen and (max-width: 992px) {
		.card {
			grid-template-columns: 1fr;
			row-gap: 50px;
			column-gap: 0;
		}
	}
</style>
