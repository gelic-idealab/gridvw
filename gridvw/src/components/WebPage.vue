<template>
  <div class="web-page">
    <!-- <div class="container"> -->
      <!-- <div class="row">
        <input v-model="localUrl" placeholder="url" id="url" type="text" v-on:change="onUpdate">
        <label for="url">Component URL</label>
      </div> -->
      <div class="row">
        <iframe v-bind:src="localUrl" frameborder=0 width="100%" :height="h"></iframe>
      </div>
    <!-- </div> -->
  </div>
</template>

<script>
export default {
  name: 'WebPage',
  props: {
    url: String,
    title: String,
    h: Number
  },
  data() {
    return {
      localUrl: this.url
    }
  },
  methods: {
      onUpdate() {
        this.$emit('update:url', this.localUrl)
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
