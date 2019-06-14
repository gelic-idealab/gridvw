<template>
  <div id="app">
    
    <a class="btn-floating btn-large waves-effect waves-light blue" v-on:click="addItem"><i class="material-icons">add</i></a>
    
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
          title: "",
          x:0,
          y:0,
          w:4,
          h:10
        },
        {
          i: 1,
          url: "https://library.illinois.edu",
          title: "",
          x:4,
          y:0,
          w:4,
          h:10
        },
        {
          i: 2,
          url: "https://library.illinois.edu/enx",
          title: "",
          x:8,
          y:0,
          w:4,
          h:10
        }
      ],
    }
  },
  methods: {
    addItem: function() {
      this.items.push({
        i: this.items.length+1,
        url: "",
        title: "",
        x:0,
        y:0,
        w:4,
        h:10
      })
    }
  }
}
</script>

<style>
#app {
  height: 100vh
}

</style>
