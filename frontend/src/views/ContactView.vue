<template>
	<div id="contact-page">
		<header
			class="contact-header"
			:style="{ 'background-image': 'url(' + banner_bg + ')' }"
		>
			<h1 class="display-text">
				Contact <span class="blue-text">Us</span>
			</h1>
		</header>

		<!-- CONTACT SECTION -->
		<section class="contact-section">
			<div class="container">
				<div class="section__header">
					<img src="@/assets/img/icons/sections/hands.svg" alt="" />
					<div class="section__titles">
						<p class="" style="opacity: 0.8">
							<span class="gold-text">//</span> CONTACT US
						</p>
						<h2 class="">Let’s build something awesome together</h2>
					</div>
				</div>
				<!-- CONTACT INFO -->
				<div class="contact-info">
					<div class="info-card">
						<div class="info-inner">
							<h6 class="info-tag bg-gold">Mail</h6>
							<hr />
							<div class="info-details">
								<h5>
									<img
										src="@/assets/img/icons/contact/mail.svg"
										alt=""
									/>
									Email
								</h5>
								<p>avpromoteagency@gmail.com</p>
							</div>
						</div>
					</div>
					<div class="info-card">
						<div class="info-inner">
							<h6 class="info-tag bg-gold">Call</h6>
							<hr />
							<div class="info-details">
								<h5>
									<img
										src="@/assets/img/icons/contact/phone.svg"
										alt=""
									/>
									Phone
								</h5>
								<p>+998 90 004-61-99</p>
							</div>
						</div>
					</div>
				</div>

				<!-- CONTACT FORM -->
				<form action="" class="contact-form" @submit="handleSubmit">
					<div>
						<label for="full_name">
							<h6>Full Name *</h6>
							<input
								type="text"
								id="full_name"
								name="full_name"
								v-model="formData.full_name"
								placeholder="John David"
								required
							/>
						</label>
						<label for="email">
							<h6>Email *</h6>
							<input
								type="email"
								id="email"
								name="email"
								v-model="formData.email"
								placeholder="mymail@example.com"
								required
							/>
						</label>
						<label for="company">
							<h6>Company *</h6>
							<input
								type="text"
								id="company"
								name="company"
								v-model="formData.company"
								placeholder="Company Name"
								required
							/>
						</label>
						<label for="subject">
							<h6>Subject *</h6>
							<input
								type="text"
								id="subject"
								name="subject"
								v-model="formData.subject"
								placeholder="How Can We Help"
								required
							/>
						</label>
					</div>
					<label for="message">
						<h6>Message *</h6>
						<textarea
							type="text"
							id="message"
							name="message"
							v-model="formData.message"
							placeholder="Hello there. I would like to talk about how to..."
							required
						/>
					</label>
					<div class="btn-wrapper">
						<button type="submit">Sent Message</button>
					</div>
				</form>
			</div>
		</section>

		<!-- FAQs -->
		<section class="faq-section">
			<div class="container">
				<div class="section__header">
					<img src="@/assets/img/icons/sections/message.svg" alt="" />
					<div class="section__titles">
						<p class="" style="opacity: 0.8">
							<span class="gold-text">//</span> FAQ
						</p>
						<h2 class="">Frequently Asked Questions</h2>
					</div>
				</div>
				<div class="faq-container">
					<div
						:class="{
							faq: true,
							active: faq.id == activeFAQ,
						}"
						v-for="faq in faqs"
						:key="faq.id"
					>
						<h4
							class="faq-title"
							@click="
								activeFAQ != faq.id
									? (activeFAQ = faq.id)
									: (activeFAQ = -1)
							"
						>
							{{ faq.question }}
							<span>{{ activeFAQ != faq.id ? "+" : "-" }}</span>
						</h4>
						<p class="faq-text">{{ faq.answer }}</p>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup>
	import banner_bg from "@/assets/img/about/about-banner.png";
	import { $axios } from "@/plugins/axios";
	import { onMounted, reactive, ref } from "vue";

	// Variables
	const formData = {
		full_name: "",
		company: "",
		email: "",
		subject: "",
		message: "",
	};
	let faqs = ref();
	let activeFAQ = ref(-1);

	// Methods
	const handleSubmit = async () => {
		await $axios.post("/contacts/", formData);
		formData.full_name = "";
		formData.company = "";
		formData.email = "";
		formData.subject = "";
		formData.message = "";
		console.log(formData);
	};
	const getFaqs = async (url) => {
		const response = await $axios.get(url);
		faqs.value = response.data;
		console.log(response.data);
	};

	// Life Cycle
	onMounted(() => {
		getFaqs("/faqs/");
	});
</script>

<style scoped>
	#contact-page {
		width: 100%;
	}
	.contact-header {
		width: 100%;
		height: 60vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-repeat: no-repeat;
		background-position: center top;
	}

	#contact-page .section__header {
		flex-direction: column;
		row-gap: 24px;
		text-align: center;
	}
	/* CONTACT INFO */
	.contact-info {
		display: flex;
		align-items: center;
		justify-content: space-evenly;
		gap: 30px;
		margin: 60px 0px;
	}
	.info-card {
		max-width: 480px;
		width: 100%;
		padding: 25px;
		border-radius: 8px;
		background: linear-gradient(
			111.05deg,
			#e9f7ff 9.66%,
			#ffdbd5 57.52%,
			#fff3ca 103.42%
		);
		text-align: center;
	}
	.info-inner {
		padding: 20px;
		background: #fff;
		border-radius: 8px;
	}
	.info-tag {
		margin: 0px auto;
		max-width: min-content;
		padding: 6px 26px;
		border-radius: 60px;
	}
	.info-card hr {
		margin: 17px 0px;
	}

	/* CONTACT FORM */
	.contact-form {
		background: linear-gradient(151.16deg, #fff8f8 10.38%, #f5f7ff 95.44%);
		width: 100%;
		padding: 80px 100px;
		border-radius: 8px;
	}
	.contact-form h6 {
		margin-bottom: 12px;
	}
	.contact-form input,
	.contact-form textarea {
		background: #ffffff;
		border: 1px solid #dcdcdc;
		border-radius: 8px;
		padding: 18px 30px;
		color: #555555;
		width: 100%;
	}
	.contact-form textarea {
		min-height: 300px;
		resize: none;
		overflow-y: scroll;
	}
	.contact-form div {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 40px;
		margin-bottom: 40px;
	}
	.contact-form div.btn-wrapper {
		margin-top: 40px;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.contact-form div.btn-wrapper button {
		border: none;
		padding: 16px 36px;
		border-radius: 8px;
		color: #fff;
		background-color: var(--secondary-dark);
		cursor: pointer;
		transition: all 0.2s ease-in-out;
	}
	.contact-form div.btn-wrapper button:focus {
		opacity: 0.9;
	}

	/* FAQs */
	.faq-container {
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		row-gap: 20px;
	}
	.faq {
		max-width: 900px;
		width: 100%;
		padding: 24px 32px;
		border-radius: 12px;
		border: 1px solid #dcdcdc;
	}
	.faq .faq-title {
		display: flex;
		justify-content: space-between;
		align-items: center;
		column-gap: 40px;
		cursor: pointer;
	}
	.faq .faq-title span {
		display: flex;
		min-width: 40px;
		min-height: 40px;
		justify-content: center;
		align-items: center;
		border-radius: 50%;
		background-color: var(--secondary-dark);
		color: #fff;
	}
	.faq .faq-text {
		font-size: calc(var(--body-text) * 1.175);
		height: 0;
		overflow: hidden;
		transition: all 0.3s ease;
	}

	.faq.active {
		background: linear-gradient(
			124.11deg,
			#e9f7ff 5.58%,
			#ffdbd5 21.8%,
			#fff3ca 37.36%
		);
	}
	.faq.active .faq-text {
		height: max-content;
		margin: 30px 0px;
	}

	/* MEDIA */
	@media screen and (max-width: 768px) {
		.contact-info {
			flex-direction: column;
		}
		.contact-form {
			padding: 40px 40px;
		}
		.contact-form div {
			display: grid;
			grid-template-columns: 1fr;
			gap: 25px;
			margin-bottom: 25px;
		}
	}
</style>
