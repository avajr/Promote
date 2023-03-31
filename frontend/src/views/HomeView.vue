<template>
	<div id="home">
		<!-- HEADER BANNER -->
		<header
			id="header"
			class="header"
			:style="{ 'background-image': 'url(' + banner_bg + ')' }"
		>
			<div class="container header__content-wrapper">
				<img
					class="header__img"
					src="@/assets/img/home/banner-img.png"
					alt=""
				/>
				<div class="header__content">
					<p><span class="gold-text">//</span> AGENCY</p>
					<h1 class="display-text">
						A fully integrated<br />digital
						<span class="blue-text">marketing</span><br />agency
					</h1>
					<p class="header__content___text">
						Lorem ipsum dolor sit amet, ea mundi malorum cum,
						ocurreret<br />reprehendunt ius ex. Ut vis mazim
						erroribus forensibus.
					</p>
					<div class="header__btns">
						<CtaBtnOutline cta="Contact Us" link="/contact/" />
					</div>
				</div>
			</div>
		</header>

		<!-- SERVICES -->
		<section id="services" class="bg-dark">
			<div class="container">
				<div class="services__content">
					<div class="section__header">
						<img
							src="@/assets/img/icons/sections/gears-blue.svg"
							alt=""
						/>
						<div class="section__titles">
							<p class="light-text" style="opacity: 0.8">
								<span class="gold-text">//</span> OUR SERVICES
							</p>
							<h2 class="light-text">
								High-impact services to take your business to
								the next level
							</h2>
						</div>
					</div>
					<div class="services-list">
						<div
							class="service-card"
							v-for="service in servicesData"
							:key="service.id"
						>
							<div class="service-card__icon">
								<img :src="service.icon" alt="" />
							</div>
							<h5 class="service-card__title light-text">
								{{ service.name }}
							</h5>
							<p class="light-text" style="opacity: 0.7">
								{{ service.description }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- TESTIMONIAL -->
		<section class="testimonial-section">
			<div class="container">
				<div class="section__header">
					<img src="@/assets/img/icons/sections/message.svg" alt="" />
					<div class="section__titles">
						<p><span class="gold-text">//</span> TESTIMONIAL</p>
						<h2>
							We work with customers<br />across all industries
						</h2>
					</div>
				</div>
				<Swiper
					:slides-per-view="2"
					:space-between="20"
					:breakpoints="swiperOptions.breakpoints"
					:pagination="{
						clickable: true,
					}"
					:modules="swiperOptions.modules"
				>
					<swiper-slide
						:key="testimonial.id"
						v-for="testimonial in testimonialData"
					>
						<div class="testimonial__inner">
							<div class="testimonial__content">
								<div class="testimonial__content___company">
									<img :src="testimonial.company" alt="" />
									<h5>Company</h5>
								</div>
								<hr />
								<p>{{ testimonial.feedback }}</p>
							</div>
							<div class="testimonial__author">
								<div class="testimonial__author___wrapper">
									<img
										:src="testimonial.client_picture"
										alt=""
									/>
								</div>
								<div class="testimonial__author___info">
									<h6>{{ testimonial.client_full_name }}</h6>
									<p>{{ testimonial.client_job.job }}</p>
								</div>
							</div>
						</div>
					</swiper-slide>
					<swiper-slide
						:key="testimonial.id"
						v-for="testimonial in testimonialData"
					>
						<div class="testimonial__inner">
							<div class="testimonial__content">
								<div class="testimonial__content___company">
									<img :src="testimonial.company" alt="" />
									<h5>Company</h5>
								</div>
								<hr />
								<p>{{ testimonial.feedback }}</p>
							</div>
							<div class="testimonial__author">
								<div class="testimonial__author___wrapper">
									<img
										:src="testimonial.client_picture"
										alt=""
									/>
								</div>
								<div class="testimonial__author___info">
									<h6>{{ testimonial.client_full_name }}</h6>
									<p>{{ testimonial.client_job.job }}</p>
								</div>
							</div>
						</div>
					</swiper-slide>
					<swiper-slide
						:key="testimonial.id"
						v-for="testimonial in testimonialData"
					>
						<div class="testimonial__inner">
							<div class="testimonial__content">
								<div class="testimonial__content___company">
									<img :src="testimonial.company" alt="" />
									<h5>Company</h5>
								</div>
								<hr />
								<p>{{ testimonial.feedback }}</p>
							</div>
							<div class="testimonial__author">
								<div class="testimonial__author___wrapper">
									<img
										:src="testimonial.client_picture"
										alt=""
									/>
								</div>
								<div class="testimonial__author___info">
									<h6>{{ testimonial.client_full_name }}</h6>
									<p>{{ testimonial.client_job.job }}</p>
								</div>
							</div>
						</div>
					</swiper-slide>
					<swiper-slide
						:key="testimonial.id"
						v-for="testimonial in testimonialData"
					>
						<div class="testimonial__inner">
							<div class="testimonial__content">
								<div class="testimonial__content___company">
									<img :src="testimonial.company" alt="" />
									<h5>Company</h5>
								</div>
								<hr />
								<p>{{ testimonial.feedback }}</p>
							</div>
							<div class="testimonial__author">
								<div class="testimonial__author___wrapper">
									<img
										:src="testimonial.client_picture"
										alt=""
									/>
								</div>
								<div class="testimonial__author___info">
									<h6>{{ testimonial.client_full_name }}</h6>
									<p>{{ testimonial.client_job.job }}</p>
								</div>
							</div>
						</div>
					</swiper-slide>
					<swiper-slide
						:key="testimonial.id"
						v-for="testimonial in testimonialData"
					>
						<div class="testimonial__inner">
							<div class="testimonial__content">
								<div class="testimonial__content___company">
									<img :src="testimonial.company" alt="" />
									<h5>Company</h5>
								</div>
								<hr />
								<p>{{ testimonial.feedback }}</p>
							</div>
							<div class="testimonial__author">
								<div class="testimonial__author___wrapper">
									<img
										:src="testimonial.client_picture"
										alt=""
									/>
								</div>
								<div class="testimonial__author___info">
									<h6>{{ testimonial.client_full_name }}</h6>
									<p>{{ testimonial.client_job.job }}</p>
								</div>
							</div>
						</div>
					</swiper-slide>
				</Swiper>
			</div>
		</section>

		<!-- BENEFITS -->
		<section class="benefits-section">
			<div class="container">
				<div class="benefits__inner">
					<div class="section__header">
						<img
							src="@/assets/img/icons/sections/star.svg"
							alt=""
						/>
						<div class="section__titles">
							<p>
								<span class="gold-text">//</span>
								BENEFITS
							</p>
							<h2>Benefits of working with<br />Maruncy</h2>
						</div>
					</div>
					<div class="benefits__inner-content">
						<div class="left">
							<div class="img-wrapper">
								<img
									src="@/assets/img/home/dashboard.png"
									alt=""
								/>
							</div>
						</div>
						<div class="right">
							<div class="benefit-card">
								<div class="icon-wrapper">
									<img
										src="@/assets/img/icons/sections/bars.svg"
										alt=""
									/>
								</div>
								<div class="benefit-card__content">
									<h5>Page Rankings</h5>
									<p>
										Lorem Ipsum is simply dummy text of the
										printing and typesetting industry.
									</p>
								</div>
							</div>
							<div class="benefit-card">
								<div class="icon-wrapper">
									<img
										src="@/assets/img/icons/sections/gears.svg"
										alt=""
									/>
								</div>
								<div class="benefit-card__content">
									<h5>Site Optimisation</h5>
									<p>
										Lorem Ipsum is simply dummy text of the
										printing and typesetting industry.
									</p>
								</div>
							</div>
							<div class="benefit-card">
								<div class="icon-wrapper">
									<img
										src="@/assets/img/icons/sections/pie-chart.svg"
										alt=""
									/>
								</div>
								<div class="benefit-card__content">
									<h5>Reporting & Analysis</h5>
									<p>
										Lorem Ipsum is simply dummy text of the
										printing and typesetting industry.
									</p>
								</div>
							</div>
							<div style="text-align: center">
								<CtaBtnOutline cta="About us" link="/about/" />
							</div>
						</div>
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
	// Components
	import banner_bg from "@/assets/img/home/banner-bg.jpg";
	import CtaBtn from "@/components/CtaBtn.vue";
	import CtaBtnOutline from "@/components/CtaBtnOutline.vue";
	import CtaBtnWhite from "@/components/CtaBtnWhite.vue";
	// Vue
	import { onMounted, reactive, ref } from "vue";
	import { $axios } from "@/plugins/axios";

	// Variable Data
	let testimonialData = ref();
	let servicesData = ref();
	const swiperOptions = reactive({
		breakpoints: {
			0: {
				slidesPerView: 1,
			},
			1025: {
				slidesPerView: 2,
			},
		},
		modules: [Pagination],
	});

	// Methods
	const getTestimonials = async (url) => {
		const response = await $axios.get(url);
		testimonialData.value = await response.data;
		console.log(response);
	};
	const getServices = async (url) => {
		const response = await $axios.get(url);
		servicesData.value = await response.data;
		console.log(response);
		console.log(servicesData.value);
	};

	// Life Cycles
	onMounted(() => {
		getTestimonials("/testimonials/");
		getServices("/services/");
	});
</script>

<style scoped>
	/* HEADER BANNER */
	#home {
		width: 100%;
	}
	#header {
		width: 100%;
		background-repeat: no-repeat;
		background-size: cover;
	}
	.header__content-wrapper {
		position: relative;
		z-index: 100;
		padding: 12% 2%;
	}
	img.header__img {
		position: absolute;
		width: 45%;
		height: auto;
		top: 50%;
		right: 0;
		z-index: -10;
		transform: translateY(-60%);
	}
	.header__content {
		max-width: 740px;
		width: 100%;
	}
	.header__content___text {
		margin: 3% 0px;
	}
	.header__btns {
		display: flex;
		column-gap: 20px;
	}

	/* SERVICES */
	.services-list {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 50px;
	}
	.service-card {
		border-radius: 30px;
		padding: 40px;
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: 20px;
		background: linear-gradient(180deg, #36363e 0%, #292930 100%);
		border: 1px solid #424249;
	}
	.service-card__icon {
		max-width: 150px;
		max-height: 150px;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: var(--secondary-dark);
		border-radius: 50%;
		padding: 2rem;
	}
	.service-card__icon img {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}

	/* TESTIMONIAL */
	.section__header {
		display: flex;
		align-items: center;
		padding: 0px 10px;
		margin-bottom: 40px;
		column-gap: 20px;
	}
	.swiper-slide {
		border-radius: 8px;
		background: linear-gradient(151.16deg, #fff8f8 10.38%, #f5f7ff 95.44%);
		padding: 32px;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #fff;
		margin-bottom: 40px;
	}
	.testimonial__content {
		background: #fff;
		border-radius: 8px;
		box-shadow: 0px 2px 4px #92929225;
		padding: 48px 32px;
	}
	.testimonial__content hr {
		margin: 20px 0px;
		opacity: 0.4;
	}
	.testimonial__content___company,
	.testimonial__author {
		display: flex;
		column-gap: 12px;
	}
	.testimonial__author {
		padding: 32px 0px;
	}
	.testimonial__author___wrapper {
		width: 60px;
		height: 60px;
		border-radius: 50%;
	}
	.testimonial__author___wrapper img {
		object-fit: cover;
	}

	/* BENEFITS */
	.benefits__inner-content {
		display: grid;
		gap: 48px;
		grid-template-columns: 1fr 1fr;
	}
	.section__header {
		display: flex;
		column-gap: 40px;
		margin-bottom: 32px;
		align-items: center;
	}
	.benefits-section .img-wrapper {
		margin: 0 auto;
	}
	.benefits-section .img-wrapper img {
		width: 100%;
		object-fit: cover;
	}
	.benefit-card {
		display: flex;
		column-gap: 16px;
	}
	.benefits__inner-content .right {
		display: flex;
		flex-direction: column;
		row-gap: 40px;
	}

	/* RESPONSIVE | MEDIA */
	@media screen and (max-width: 1090px) {
		img.header__img {
			position: initial;
			width: 40%;
			transform: none;
			align-self: center;
		}
		.header__content-wrapper {
			display: flex;
			flex-direction: row-reverse;
			padding: 8rem 1rem;
		}
	}
	@media screen and (max-width: 768px) {
		img.header__img {
			display: none;
		}
		.benefits__inner-content {
			grid-template-columns: 1fr;
		}
		.benefits-section .img-wrapper {
			text-align: center;
		}
		.benefits-section .img-wrapper img {
			width: 60%;
			justify-self: center;
		}
	}
	@media screen and (max-width: 470px) {
		.section__header {
			flex-direction: column;
			row-gap: 40px;
		}
		.section__titles {
			text-align: center;
		}
	}
	@media screen and (max-width: 375px) {
		.header__btns {
			flex-direction: column;
			row-gap: 20px;
		}
		.header__btns .cta {
			width: max-content;
		}
	}
</style>
