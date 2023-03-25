<template>
	<nav class="navbar">
		<div class="container nav">
			<div class="navbar__logo">
				<img src="@/assets/img/Logo-dark.png" alt="Logo" />
			</div>
			<ul :class="{ 'navbar__nav-links': true, active: isMenuOpen }">
				<li class="nav-link">
					<router-link to="/">Home</router-link>
				</li>
				<li class="nav-link">
					<router-link to="/about/">About</router-link>
				</li>
				<li class="nav-link">
					<router-link to="/services/">Services</router-link>
				</li>
				<li class="nav-link">
					<router-link to="/blog/">Blog</router-link>
				</li>
				<li class="nav-cta cta">
					<router-link to="/contact/" class="nav-link nav-cta"
						>Contact us</router-link
					>
				</li>
			</ul>
			<button class="menu-btn" @click="menuHandler()">
				<img
					v-if="!isMenuOpen"
					src="@/assets/img/icons/sections/menu.svg"
					alt="menu"
				/>
				<img
					v-else
					src="@/assets/img/icons/sections/close.svg"
					alt="menu"
				/>
			</button>
		</div>
	</nav>
</template>

<script setup>
	import { ref } from "vue";
	let isMenuOpen = ref(false);

	const menuHandler = () => {
		isMenuOpen.value = !isMenuOpen.value;
	};
</script>

<style scoped>
	.navbar {
		position: absolute;
		width: 100%;
		top: 0;
		left: 0;
		z-index: 1000;
	}
	.navbar .nav {
		display: flex;
		padding: 10px;
		justify-content: space-between;
		align-items: center;
		height: 80px;
		z-index: 1000;
	}
	.navbar__logo {
		height: 80px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.navbar__logo img {
		height: 60px;
	}
	.navbar__nav-links {
		max-width: 480px;
		width: 75%;
		height: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.nav-link {
		list-style: none;
		height: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.nav-link a {
		text-decoration: none;
		color: var(--secondary-dark);
		font-weight: 500;
	}
	.nav-link a.router-link-active {
		border-bottom: 3px solid var(--primary-blue);
	}
	.nav-link a:hover {
		border-bottom: 3px solid var(--primary-gold);
	}
	.nav-cta {
		list-style: none;
		background-color: var(--secondary-dark);
		border-radius: 8px;
	}
	.nav-cta a:hover {
		background-color: var(--primary-blue);
	}
	.nav-cta a {
		padding: 20px 40px;
		text-decoration: none;
		font-weight: 500;
		width: 100%;
		height: 100%;
		color: var(--secondary-light);
	}

	.menu-btn {
		display: none;
		border: none;
		background-color: transparent;
		cursor: pointer;
	}

	@media screen and (max-width: 768px) {
		.menu-btn {
			display: block;
		}
		.nav {
			position: relative;
		}
		.navbar__nav-links {
			position: absolute;
			top: 0;
			left: 0;
			z-index: -10;
			padding-top: 80px;
			max-width: 100vw !important;
			width: 100%;
			height: 0px;
			flex-direction: column;
			justify-content: start;
			background: transparent;
			overflow: hidden;
		}
		.navbar__nav-links.active {
			height: 100vh;
			background-color: #fff;
		}
		.nav-link {
			font-size: 1.4rem;
			height: 80px;
		}
	}
</style>
