<template>
  <div id="app">

    <div class="grid">
      <div class="item" v-for="cell in cells" :key="cell.id">
        <div class="item-content">
          <web-page :url="cell.url" :title="cell.title"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import WebPage from './components/WebPage.vue'
import Muuri from 'muuri';

export default {
  name: 'app',
  components: {
    WebPage
  },
  data() {
    return {
      cells: [
        {
          id: 0,
          url: "https://nytimes.com",
          title: "NY Times"
        },
        {
          id: 1,
          url: "https://library.illinois.edu",
          title: "Library"
        },
        {
          id: 2,
          url: "https://library.illinois.edu/enx",
          title: "Grainger"
        }
      ],
      grid: null
    }
  },
  mounted() {
    this.grid = new Muuri('.grid', {
      dragEnabled: true,
      layout: {
        fillGaps: true,
        rounding: false
        }
  });
  }
}
</script>

<style>

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
