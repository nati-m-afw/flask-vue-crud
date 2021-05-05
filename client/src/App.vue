<template>
  <div class="app">
    <router-view />
  </div>
</template>

<script>
export default {
  watch: {
    $route(to) {
      document.title = to.meta.title ? to.meta.title + ' - ' + 'Flask Vue CRUD' : "Flask-Vue CRUD";
    },
  },
};
</script>
