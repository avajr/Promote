<template>
	<div id="case-study-page">
		<header
			class="case-study-header"
			:style="{ 'background-image': 'url(' + banner_bg + ')' }"
		>
			<h1 class="display-text">
				Our <span class="blue-text">Blog</span>
			</h1>
		</header>
		<section id="case-studies">
			<div class="container">
				<div class="section__header">
					<img src="@/assets/img/icons/sections/doc.svg" alt="" />
					<div class="section__titles">
						<p class="" style="opacity: 0.8">
							<span class="gold-text">//</span> ARTICLES
						</p>
						<h2 class="">Browse our content on growth marketing</h2>
					</div>
          <div class="search_block">
            <input class="search_box" type="text" placeholder="Search the blog ..." v-on:input="getBlogs" v-model="searchInput" />
            <input class="search_btn" type="button" value="Search"/>
          </div>
				</div>
				<div class="case-studies-list">
					<ul>
						<li
							class="card"
							v-for="blog in paginatedData"
							:key="blog.id"
						>
							<div class="card-img">
								<img :src="blog.cover_img" alt="" />
							</div>
							<div class="card-content">
								<div
									class="card-content-top"
									style="margin-bottom: 20px"
								>
									<span>{{ blog.created_at }}</span>
								</div>
								<h5 style="font-weight: 600">
									{{ blog.title }}
								</h5>
								<p>{{ blog.short_description }}</p>
								<router-link
									class="btn"
									:to="`/blog/${blog.id}`"
									>Read More</router-link
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

	let blogs = ref();

	const data = ref([]);

  let searchInput = '';

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


  const getBlogs = async (args=null) => {
		const response = await $axios.get(`/blogs/?search=${searchInput}`);
		blogs.value = response.data;
		data.value = response.data;
		console.log(searchInput);
	};

	// Life Cycle
	onMounted(() => {
		getBlogs();
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
		flex-direction: row;
		row-gap: 24px;
		text-align: left;
	}

	.card {
		min-height: 480px;
		list-style: none;
		display: grid;
		grid-template-columns: 1fr 1fr;
		column-gap: 50px;
		width: 100%;
		padding: 50px;
		background: #fff3ca;
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
		background-color: transperant;
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

  .search_block {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .search_box {
		background: #ffffff;
		border: 1px solid #dcdcdc;
		border-radius: 8px;
		padding: 18px 30px;
		color: #555555;
		flex-grow: 3;
    flex-wrap: wrap;
    font-size: 1rem;
	}

  .search_btn {
		background-color: var(--secondary-dark);
		border-radius: 8px;
	}
	.search_btn:hover {
		background-color: var(--primary-blue);
	}
	.search_btn {
		padding: 20px 40px;
		text-decoration: none;
		font-weight: 500;
		flex-grow: 1;
		height: 100%;
		color: var(--secondary-light);
	}

	/* MEDIA */
	@media screen and (max-width: 992px) {
		.card {
			grid-template-columns: 1fr;
			column-gap: 0;
      padding: 30px;
		}
    .card-content {
      padding: 30px 10px;
    }
    .btn {
      width: 100%;
    }
    #case-study-page .section__header {
      flex-direction: column;
      text-align: center;
    }
    .search_block {
      width: 100%;
    }
	}@media screen and (max-width: 460px) {
		.card {
			grid-template-columns: 1fr;
			column-gap: 0;
      padding: 30px;
		}
    .card-content {
      padding: 30px 10px;
    }
    #case-study-page .section__header {
      flex-direction: column;
      text-align: center;
    }
    .search_block {
      width: 100%;
      flex-direction: column;
    }
    .search_box, .search_btn {
      width: 100%;
    }
	}
</style>
