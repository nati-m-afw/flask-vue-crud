import Vue from "vue";
import VueRouter from "vue-router";
import Ping from '../components/Ping.vue';
import Books from '../components/Books.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
  {
    path: "/",
    name: "Books",
    component: Books,
    meta: {title: "Books"},
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title ? to.meta.title + ' - ' + 'Flask Vue CRUD' : "Flask-Vue CRUD";
  next();
});

export default router;
