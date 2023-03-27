<template>
	<div id="about-page">
		<header
			class="about-header"
			:style="{ 'background-image': 'url(' + banner_bg + ')' }"
		>
			<h1 class="display-text">
				About <span class="blue-text">Us</span>
			</h1>
		</header>
		<!-- ABOUT NUMBERS -->
		<section id="about-numbers" class="about-numbers bg-dark">
			<div>
				<h2 class="light-text">
					325<span style="color: blue">+</span>
				</h2>
				<p class="sm-text light-text" style="opacity: 0.7">
					CLIENTS<br />
					WORLDWIDE
				</p>
			</div>
			<div>
				<h2 class="light-text">975<span style="color: red">+</span></h2>
				<p class="sm-text light-text" style="opacity: 0.7">
					PROJECTS<br />COMPLETED
				</p>
			</div>
			<div>
				<h2 class="light-text">
					70<span style="color: green">+</span>
				</h2>
				<p class="sm-text light-text" style="opacity: 0.7">
					TEAM<br />
					MEMBERS
				</p>
			</div>
		</section>
		<!-- ABOUT US -->
		<section id="aboutus">
			<div class="container">
				<div class="aboutus__content-wrapper">
					<div class="aboutus__img-wrapper">
						<img src="@/assets/img/about/aboutus.png" alt="" />
					</div>
					<div class="aboutus__content">
						<div class="section__header">
							<img
								src="@/assets/img/icons/sections/at-symbol.svg"
								alt=""
							/>
							<div class="section__titles">
								<p>
									<span class="gold-text">//</span> ABOUT US
								</p>
								<h2>
									The #1 digital marketing<br />services
									company
								</h2>
							</div>
						</div>
						<hr />
						<p
							class="aboutus__content___text"
							style="text-align: left"
						>
							Lorem ipsum dolors sit non amet consectetur
							adipiscing elit fringilla aliquam Aliquam vestibulum
							libero morbi blandit cursus risus. Laoreet non
							curabitur gravida arcu ac tortor semper vivera nam
							libero justo laoreet mollis aliquam ut porttitor leo
							a diam.
						</p>
						<div>
							<CtaBtnOutline
								cta="Get In Touch"
								link="/contact/"
							/>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- VALUES -->
		<section id="values" class="bg-dark">
			<div class="container">
				<div class="values__content">
					<div class="section__header">
						<img
							src="@/assets/img/icons/sections/tick.svg"
							alt=""
						/>
						<div class="section__titles">
							<p class="light-text" style="opacity: 0.8">
								<span class="gold-text">//</span> OUR VALUES
							</p>
							<h2 class="light-text">
								The core values behind our work
							</h2>
						</div>
					</div>
					<Swiper
						:slides-per-view="3"
						:space-between="20"
						:breakpoints="swiperOptions.breakpoints"
						:pagination="{
							clickable: true,
						}"
						:modules="swiperOptions.modules"
					>
						<SwiperSlide>
							<ValueCard
								:icon="gear_blue"
								title="Efficency"
								text="Lorem ipsum dolor sit amet consecte tur adipiscing elit olme do semper dalaracc lacus vel facilisis volutpat est velitolm."
							/>
						</SwiperSlide>
						<SwiperSlide>
							<ValueCard
								:icon="tick_icon"
								title="Accountability"
								text="Lorem ipsum dolor sit amet consecte tur adipiscing elit olme do semper dalaracc lacus vel facilisis volutpat est velitolm."
							/>
						</SwiperSlide>
						<SwiperSlide>
							<ValueCard
								:icon="statistics_icon"
								title="Commitment"
								text="Lorem ipsum dolor sit amet consecte tur adipiscing elit olme do semper dalaracc lacus vel facilisis volutpat est velitolm."
							/>
						</SwiperSlide>
						<SwiperSlide>
							<ValueCard
								:icon="component_icon"
								title="Team Work"
								text="Lorem ipsum dolor sit amet consecte tur adipiscing elit olme do semper dalaracc lacus vel facilisis volutpat est velitolm."
							/>
						</SwiperSlide>
					</Swiper>
				</div>
			</div>
		</section>

		<section id="team">
			<div class="container">
				<div class="section-inner">
					<div class="section__header">
						<img
							src="@/assets/img/icons/sections/tick.svg"
							alt=""
						/>
						<div class="section__titles">
							<p class="" style="opacity: 0.8">
								<span class="gold-text">//</span> OUR TEAM
							</p>
							<h2 class="">Our team of expert marketers</h2>
						</div>
					</div>
					<div class="team__members">
						<Swiper
							:slides-per-view="1"
							:space-between="20"
							:breakpoints="swiperStaffOptions.breakpoints"
							:pagination="{
								clickable: true,
							}"
							:modules="swiperStaffOptions.modules"
						>
							<SwiperSlide
								class="staff-card"
								v-for="staff in staffData"
								:key="staff.id"
							>
								<div class="staff-picture">
									<img :src="staff.picture" alt="" />
								</div>
								<div>
									<h5>{{ staff.first_name }}</h5>
									<h5>{{ staff.last_name }}</h5>
									<p>{{ staff.job.job }}</p>
								</div>
								<div class="socials">
									<a
										:href="staff.instagram_url"
										v-if="staff.instagram_url"
									>
										<img
											src="@/assets/img/icons/socials/Instagram.svg"
											alt=""
										/>
									</a>
									<a
										:href="staff.facebook_url"
										v-if="staff.instagram_url"
									>
										<img
											src="@/assets/img/icons/socials/Facebook.svg"
											alt=""
										/>
									</a>
									<a
										:href="staff.twitter_url"
										v-if="staff.instagram_url"
									>
										<img
											src="@/assets/img/icons/socials/Twitter.svg"
											alt=""
										/>
									</a>
								</div>
							</SwiperSlide>
						</Swiper>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup>
	// Import Swiper Vue.js components
	import { Swiper, SwiperSlide } from "swiper/vue";
	import "swiper/css";
	import "swiper/css/pagination";
	import { Pagination } from "swiper";

	// Import Components
	import banner_bg from "@/assets/img/about/about-banner.png";
	import gear_blue from "@/assets/img/icons/card/gear-blue.svg";
	import tick_icon from "@/assets/img/icons/card/tick.svg";
	import statistics_icon from "@/assets/img/icons/card/statistics.svg";
	import component_icon from "@/assets/img/icons/card/component.svg";
	import CtaBtnOutline from "@/components/CtaBtnOutline.vue";
	import ValueCard from "@/components/ValueCard.vue";

	// Vue
	import { onMounted, reactive, ref } from "vue";
	import { $axios } from "@/plugins/axios";

	const swiperOptions = reactive({
		breakpoints: {
			0: {
				slidesPerView: 1,
			},
			820: {
				slidesPerView: 2,
			},
			1190: {
				slidesPerView: 3,
			},
		},
		modules: [Pagination],
	});
	const swiperStaffOptions = reactive({
		breakpoints: {
			0: {
				slidesPerView: 1,
			},
			820: {
				slidesPerView: 2,
			},
			1190: {
				slidesPerView: 3,
			},
		},
		modules: [Pagination],
	});
	let staffData = ref();

	// Methods
	const getStaff = async (url) => {
		const response = await $axios.get(url);
		staffData.value = await response.data;
		console.log(response);
	};

	// Life Cycles
	onMounted(() => {
		getStaff("/staff/");
	});
</script>

<style scoped>
	#about-page {
		width: 100%;
	}
	.about-header {
		width: 100%;
		height: 60vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-repeat: no-repeat;
		background-position: center top;
	}

	/* ABOUT NUMBERS */
	section.about-numbers {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		column-gap: 40px;
		row-gap: 40px;
		flex-wrap: wrap;
	}
	section.about-numbers > div {
		display: flex;
		column-gap: 16px;
	}

	/* ABOUT US */
	.aboutus__content-wrapper {
		display: grid;
		column-gap: 64px;
		grid-template-columns: 0.75fr 1fr;
	}
	.aboutus__img-wrapper img {
		max-width: 480px;
		width: 100%;
		object-fit: cover;
	}
	.aboutus__content___text {
		margin: 32px 0px;
	}

	/* VALUES */
	.swiper-slide {
		max-width: 380px;
	}

	/* TEAM */
	.staff-card {
		/* max-width: 380px; */
		width: 100%;
		border: 1px solid #dcdcdc;
		border-radius: 30px;
		padding: 25px;
		margin-bottom: 40px;
	}
	.staff-card .staff-picture {
		width: 100%;
		max-height: 330px;
		height: 50%;
		border-radius: 30px 30px 0px 0px;
		overflow: hidden;
		margin-bottom: 30px;
	}

	.staff-picture img {
		width: 100%;
		object-fit: cover;
	}

	.staff-card div {
		text-align: center;
	}
	.socials {
		width: 100%;
		height: 26px;
		margin: 24px 0px;
		display: flex;
		column-gap: 8px;
		justify-content: center;
		align-items: center;
	}
	.staff-card a {
		display: inline-block;
		width: 26px;
		height: 26px;
	}
	.staff-card a img {
		width: 100%;
		object-fit: cover;
	}

	/* Responsiveness */
	@media screen and (max-width: 1024px) {
		.aboutus__content-wrapper {
			display: grid;
			row-gap: 64px;
			grid-template-columns: 0.8fr;
			justify-content: center;
			text-align: center;
		}
		.section__header {
			flex-direction: column;
			row-gap: 24px;
			text-align: center;
		}
		.aboutus__content {
			grid-row: 1;
		}
	}
	@media screen and (max-width: 768) {
	}
</style>
