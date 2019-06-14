<template>
  <div id="app">

    <grid-layout
            :layout="this.items"
            :col-num="12"
            :row-height="30"
            :is-draggable="true"
            :is-resizable="true"
            :vertical-compact="true"
            :margin="[10, 10]"
            :use-css-transforms="true"
    >

        <grid-item v-for="item in items"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i"
                   :key="item.i"
      >
        <web-page :url="item.url" :title="item.title" :h="item.h*30"/>
      </grid-item>
    </grid-layout>
  </div>
</template>

<script>
import WebPage from './components/WebPage.vue'
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'app',
  components: {
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
    WebPage
  },
  data() {
    return {
      items: [
        {
          i: 0,
          url: "https://nytimes.com",
          title: "NY Times",
          x:0,
          y:0,
          w:2,
          h:2
        },
        {
          i: 1,
          url: "https://library.illinois.edu",
          title: "Library",
          x:1,
          y:2,
          w:2,
          h:2
        },
        {
          i: 2,
          url: "https://library.illinois.edu/enx",
          title: "Grainger",
          x:2,
          y:0,
          w:2,
          h:2
        }
      ],
    }
  }
}
</script>

<style>

</style>
