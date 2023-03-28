<template>
	<footer id="footer" class="bg-dark">
		<div class="container">
			<div class="footer__content">
				<div class="footer__address bg-gray">
					<div class="footer__logo">
						<img src="@/assets/img/Logo-light.png" alt="Logo" />
					</div>
					<div class="footer__contact">
						<h5 class="light-text">
							<img
								src="@/assets/img/icons/footer/phone.svg"
								alt=""
							/>
							Get in touch with
						</h5>
						<h5 class="gold-text">+1 917 000 1212</h5>
						<p class="light-text">nextlevel@marketing.com</p>
					</div>
					<div class="footer__location">
						<h5 class="light-text">
							<img
								src="@/assets/img/icons/footer/location.svg"
								alt=""
							/>
							Location
						</h5>
						<p class="light-text">
							10 Suna House 65 Rivington Street London EC2A 3QQ
						</p>
					</div>
				</div>
				<div class="footer__nav">
					<div class="nav__cols">
						<h5 class="nav-title light-text">
							<img
								src="@/assets/img/icons/footer/pages.svg"
								alt=""
							/>
							Pages
						</h5>
						<ul>
							<li><router-link to="/">Home</router-link></li>
							<li>
								<router-link to="/about/">About</router-link>
							</li>
							<li><router-link to="/blog/">Blog</router-link></li>
							<li><a>Pricing</a></li>
							<li>
								<router-link to="/contact/"
									>Contact</router-link
								>
							</li>
							<li>
								<router-link to="/services/"
									>Services</router-link
								>
							</li>
						</ul>
					</div>
					<div class="nav__cols">
						<h5 class="nav-title light-text">
							<img
								src="@/assets/img/icons/footer/utility.svg"
								alt=""
							/>
							Utility Pages
						</h5>
						<ul>
							<li><a href="">404 Not Found</a></li>
							<li><a href="">Password Protected</a></li>
							<li><a href="">Licenses</a></li>
							<li><a href="">Changelog</a></li>
						</ul>
					</div>
					<div class="nav__cols">
						<h5 class="nav-title light-text">
							<img
								src="@/assets/img/icons/footer/follows.svg"
								alt=""
							/>
							Follows
						</h5>
						<ul>
							<li><a href="">Facebook</a></li>
							<li><a href="">Twitter</a></li>
							<li><a href="">Instagram</a></li>
							<li><a href="">LinkedIn</a></li>
						</ul>
					</div>
				</div>
			</div>
			<p id="copyright">
				Copyright &copy; Abdurakhmon Abdulkhakimov | Designed by
				VictorFlow - Powered by Webflow
			</p>
		</div>
	</footer>
</template>

<script setup></script>

<style scoped>
	#footer {
		display: block;
		padding: 20vh 0 9vh 0;
		color: var(--secondary-light);
	}
	#footer .footer__content {
		display: flex;
		justify-content: space-between;
	}
	#copyright {
		margin-top: 100px;
		padding-top: 20px;
		border-top: 1px solid var(--secondary-gray);
		text-align: center;
	}

	/* Logo */
	.footer__logo {
		width: 100%;
	}
	.footer__logo img {
		width: 100%;
	}

	/* Address */
	.footer__address {
		width: 400px;
		padding: 50px;
		border-radius: 8px;
	}
	.footer__contact,
	.footer__location {
		margin-top: 32px;
		padding-top: 16px;
		border-top: 1px solid rgba(246, 246, 246, 0.4);
		display: flex;
		flex-direction: column;
		row-gap: 8px;
	}

	/* Navigation */
	.footer__nav {
		width: 100%;
		display: flex;
		justify-content: space-evenly;
	}
	.nav-title {
		display: flex;
		align-items: center;
		column-gap: 8px;
		margin-bottom: 8px;
	}
	ul {
		list-style: none;
		font-size: 1.175rem;
	}
	ul li a {
		color: var(--secondary-light);
		text-decoration: none;
		line-height: 200%;
	}
	ul li a:hover {
		opacity: 0.6;
	}

	@media screen and (max-width: 768px) {
		.footer__address {
			width: 100%;
			text-align: center;
		}
		#footer .footer__content {
			flex-direction: column;
			align-items: center;
			row-gap: 60px;
		}
	}
	@media screen and (max-width: 546px) {
		.footer__nav {
			flex-direction: column;
			row-gap: 40px;
			text-align: center;
		}
		.nav-title {
			justify-content: center;
			margin-bottom: 26px;
		}
	}
</style>
