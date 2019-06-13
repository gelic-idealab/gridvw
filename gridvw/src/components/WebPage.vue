<template>
  <div class="web-page">
    <div class="col">
      <input v-model="url" placeholder="url" id="url" type="text">
        <label for="url">Component URL</label>
    </div>
    <!-- <input  type="text" name="Component Height"> -->
    <iframe v-bind:src="url" frameborder=0 style="width:100%;height:100%"></iframe>
  </div>
</template>

<script>
export default {
  name: 'WebPage',
  props: {
    url: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
