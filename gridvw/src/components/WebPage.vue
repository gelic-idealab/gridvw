<template>
  <div class="web-page">
    <div class="card blue-grey darken-1">
        <div class="card-content white-text">
          <span class="card-title">{{ title }}</span>
        </div>
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
