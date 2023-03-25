import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView";

const routes = [
	{
		name: "home",
		path: "/",
		component: HomeView,
	},
	{
		name: "about",
		path: "/about/",
		component: import("@/views/AboutView.vue"),
	},
	{
		name: "services",
		path: "/services/",
		component: import("@/views/ServicesView.vue"),
	},
	{
		name: "blog",
		path: "/blog/",
		component: import("@/views/BlogView.vue"),
	},
	{
		name: "contact",
		path: "/contact/",
		component: import("@/views/ContactView.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
