<template>
  <div id="app">
    <div class="grid">

      <div class="item">
        <div class="item-content">
          <WebPage />
        </div>
      </div>

      <div class="item">
        <div class="item-content">
          <WebPage />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import WebPage from './components/WebPage.vue'
import 'hammerjs';
import Muuri from 'muuri';

export default {
  name: 'app',
  components: {
    WebPage
  },
  data() {
    return {
      grid: null
    }
  },
  mounted() {
    this.grid = new Muuri('.grid', {
      dragEnabled: true,
      layout: {
        fillGaps: true,
        // horizontal: true,
        // alignRight: true,
        // alignBottom: true,
        // rounding: false
        }
  });
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

.grid {
  position: relative;
}
.item {
  display: block;
  position: absolute;
  width: 300px;
  height: 300px;
  margin: 5px;
  z-index: 1;
  /* background: #000; */
  color: #fff;
}
.item.muuri-item-dragging {
  z-index: 3;
}
.item.muuri-item-releasing {
  z-index: 2;
}
.item.muuri-item-hidden {
  z-index: 0;
}
.item-content {
  position: relative;
  width: 100%;
  height: 100%;
}
</style>
