<template>
  <div id="app">
    <v-toolbar dark color="primary">
    <v-toolbar-side-icon></v-toolbar-side-icon>

    <v-toolbar-title class="white--text">Grid Viz Wall</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn icon>
      <v-icon>search</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>apps</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>refresh</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>more_vert</v-icon>
    </v-btn>
    <v-btn fab color="black" v-on:click="addItem"><v-icon color="white">add</v-icon></v-btn>
    <v-text-field v-on:change="updatePlaceholder('colnum')"
      :label="gl.colnum.label"
      :placeholder="gl.colnum.placeholder"
      v-model.number="gl.colnum.value"
    >
    </v-text-field>
    <v-text-field v-on:change="updatePlaceholder('rowheight')"
      :label="gl.rowheight.label"
      :placeholder="gl.rowheight.placeholder"
      v-model.number="gl.rowheight.value"
    >
    </v-text-field>
  </v-toolbar>
    
    <grid-layout
            :layout="this.items"
            :col-num="gl.colnum.value"
            :row-height="gl.rowheight.value"
            :is-draggable="gl.isdraggable.value"
            :is-resizable="gl.isresizable.value"
            :vertical-compact="gl.verticalcompact.value"
            :margin="gl.margin.value"
            :use-css-transforms="gl.usecsstransforms.value"
    >

        <grid-item v-for="item in items"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i"
                   :key="item.i"
  
      >
        <web-page :title="item.title" :h="item.h*gl.rowheight.value" :url.sync="item.url" :spawn="item.spawn"/>
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
      gl: {
        colnum: { 
          label: "Columns",
          value: 12,
          placeholder:""
        },
        rowheight: { 
          label: "Row Height",
          value: 50,
          placeholder:""
        },
        isdraggable: { 
          label: "Draggable",
          value: true,
          placeholder:""
        },
        isresizable: { 
          label: "Resizable",
          value: true,
          placeholder:""
        },
        verticalcompact: { 
          label: "Vertical Compact",
          value: false
        },
        margin: { 
          label: "Margin",
          value: [0,0]
        },
        usecsstransforms: { 
          label: "Use CSS Transforms",
          value: true
        }
      },
      items: [
        {
          i: 0,
          url: "https://www.wikipedia.org/",
          title: "",
          x:0,
          y:0,
          w:2,
          h:1,
          spawn: false
        },
        {
          i: 1,
          url: "https://vuejs.org/",
          title: "",
          x:6,
          y:0,
          w:2,
          h:1,
          spawn: false
        }
      ],
    }
  },
  methods: {
    addItem: function() {
      this.items.push({
        i: this.items.length+4,
        url: "https://grainger-engineering-library.github.io/gridvw/",
        title: "",
        x:0,
        y:0,
        w:4,
        h:10,
        spawn: true
      })
    },
    componentURLUpdated(url,i) {
      this.item[i].url=url
    },
    updatePlaceholder: function(key) {
      this.gl[key].placeholder=this.gl[key].value.toString()
    }
  },
  mounted() {
    this.updatePlaceholder("colnum");
    this.updatePlaceholder("rowheight");
  }
}
</script>

<style>
#app {
  height: 100vh
}

</style>
