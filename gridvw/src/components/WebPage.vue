<template>
  <div class="web-page">
    <div class="row">
      <div class="input-field col s6">
        <input v-model="height" id="height" type="text">
        <label for="height">Component Height</label>
      </div>
      <div class="input-field col s6">
        <input v-model="width" id="width" type="text">
        <label for="width">Component Width</label>
      </div>
    </div>

    <div class="row">
      <input v-model="url" placeholder="url" id="url" type="text">
        <label for="url">Component URL</label>
    </div>
    <!-- <input  type="text" name="Component Height"> -->
    <iframe v-bind:src="url" frameborder="0" :height="height" :width="width"></iframe>
  </div>
</template>

<script>
export default {
  name: 'WebPage',
  data() {
    return {
      url: "",
      height: 0,
      width: 0
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
