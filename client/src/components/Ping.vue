<template>
  <div>
    <button class="btn btn-primary m-5">{{ msg }}</button>
  </div>
</template>

<script>
export default {
  name: "Ping",
  data() {
    return {
      msg: "Pong",
    };
  },
};
</script>
