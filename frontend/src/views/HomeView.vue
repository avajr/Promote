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
						<CtaBtn cta="Our Services" link="/services/" />
						<CtaBtnOutline cta="Contact Us" link="/contact/" />
					</div>
				</div>
			</div>
		</header>
	</div>
</template>

<script setup>
	import banner_bg from "@/assets/img/home/banner-bg.jpg";
	import CtaBtn from "@/components/CtaBtn.vue";
	import CtaBtnOutline from "@/components/CtaBtnOutline.vue";
	import CtaBtnWhite from "@/components/CtaBtnWhite.vue";
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
