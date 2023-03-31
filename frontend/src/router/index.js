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
		name: "case-study",
		path: "/case-study/",
		component: import("@/views/CaseStudyView.vue"),
	},
	{
		name: "blog",
		path: "/blog/",
		component: import("@/views/BlogView.vue"),
	},
	{
		name: "blog-detail",
		path: "/blog/:id",
		component: import("@/views/BlogDetailView.vue"),
	},
	{
		name: "contact",
		path: "/contact/",
		component: import("@/views/ContactView.vue"),
	},
	{
		name: "case-study-detail",
		path: "/case-study/:id",
		component: import("@/views/CaseStudyDetailView.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
