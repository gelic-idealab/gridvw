<template>
  <div id="app">
    <WebPage />
    <WebPage />
  </div>
</template>

<script>
import WebPage from './components/WebPage.vue'

export default {
  name: 'app',
  components: {
    WebPage
  },
  data() {
    return {
      url: "https://google.com"
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
