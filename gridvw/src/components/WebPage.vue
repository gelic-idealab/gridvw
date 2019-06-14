<template>
  <div class="web-page">
    <div class="row">
      <input v-model="url" placeholder="url" id="url" type="text">
      <label for="url">Component URL</label>
    </div>
    <iframe v-bind:src="url" frameborder=0 width="100%" :height="h"></iframe>
  </div>
</template>

<script>
export default {
  name: 'WebPage',
  props: {
    url: String,
    title: String,
    h: Number
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
