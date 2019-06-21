<template>
  <div id="app">
    
    <v-btn fab color="black" v-on:click="addItem"><v-icon color="white">add</v-icon></v-btn>
    
    <grid-layout
            :layout="this.items"
            :col-num="12"
            :row-height="30"
            :is-draggable="true"
            :is-resizable="true"
            :vertical-compact="false"
            :margin="[0, 0]"
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
        <web-page :title="item.title" :h="item.h*30" :url.sync="item.url"/>
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
          url: "https://www.wikipedia.org/",
          title: "",
          x:0,
          y:0,
          w:6,
          h:10
        },
        {
          i: 1,
          url: "https://vuejs.org/",
          title: "",
          x:6,
          y:0,
          w:6,
          h:10
        }
        // {
        //   i: 2,
        //   url: "https://library.illinois.edu/enx",
        //   title: "",
        //   x:6,
        //   y:0,
        //   w:3,
        //   h:23
        // },
        // {
        //   i: 3,
        //   url: "https://3deposit.surge.sh",
        //   title: "",
        //   x:9,
        //   y:0,
        //   w:3,
        //   h:23
        // },
        // {
        //   i: 4,
        //   url: "https://www.library.illinois.edu/infosci/",
        //   title: "",
        //   x:12,
        //   y:27,
        //   w:3,
        //   h:28
        // }
      ],
    }
  },
  methods: {
    addItem: function() {
      this.items.push({
        i: this.items.length+4,
        url: "",
        title: "",
        x:0,
        y:0,
        w:4,
        h:10
      })
    },
    componentURLUpdated(url,i) {
        this.item[i].url=url
    }
  },
  // mounted() {
  //   this.items[0].url = items[0].url;
  // }
}
</script>

<style>
#app {
  height: 100vh
}

</style>
