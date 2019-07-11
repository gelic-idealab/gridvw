<template>
  <div id="view-editor">
    <v-toolbar dark color="primary">
    <v-toolbar-side-icon></v-toolbar-side-icon>

    <v-toolbar-title class="white--text text-uppercase">Grid Viz Wall</v-toolbar-title>

    <v-spacer></v-spacer>
    <v-btn fab dark v-on:click="addItem"><v-icon color="white">add</v-icon></v-btn>
    
    <v-spacer></v-spacer>
    <v-btn fab dark v-on:click="pushView"><v-icon color="white">PUSH VIEW</v-icon></v-btn>

    <v-text-field v-on:change="updatePlaceholder('colnum')"
      :label="config.gl.colnum.label"
      :placeholder="config.gl.colnum.placeholder"
      v-model.number="config.gl.colnum.value"
    >
    </v-text-field>
    <v-text-field v-on:change="updatePlaceholder('rowheight')"
      :label="config.gl.rowheight.label"
      :placeholder="config.gl.rowheight.placeholder"
      v-model.number="config.gl.rowheight.value"
    >
    </v-text-field>
  </v-toolbar>
    
    <grid-layout
            :layout="this.config.items"
            :col-num="config.gl.colnum.value"
            :row-height="config.gl.rowheight.value"
            :is-draggable="config.gl.isdraggable.value"
            :is-resizable="config.gl.isresizable.value"
            :vertical-compact="config.gl.verticalcompact.value"
            :margin="config.gl.margin.value"
            :use-css-transforms="config.gl.usecsstransforms.value"
    >

        <grid-item v-for="item in config.items"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i"
                   :key="item.i"
  
      >
        <web-page :title="item.title" :h="item.h*config.gl.rowheight.value" :url.sync="item.url" :spawn="item.spawn"/>
      </grid-item>
    </grid-layout>

  </div>
</template>

<script>
import axios from 'axios'
import WebPage from '../components/WebPage.vue'
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'view-editor',
  components: {
    GridLayout: VueGridLayout.GridLayout,
    GridItem: VueGridLayout.GridItem,
    WebPage
  },
  data() {
    return {
      config: {
        gl: {
          colnum: { 
            label: "Columns",
            value: 7680,
            placeholder:""
          },
          rowheight: { 
            label: "Row Height",
            value: 1,
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
            w:1920,
            h:500,
            spawn: false
          },
          {
            i: 1,
            url: "https://vuejs.org/",
            title: "",
            x:6,
            y:0,
            w:1920,
            h:500,
            spawn: false
          }
        ],
      }
    }
  },
  methods: {
    addItem: function() {
      this.config.items.push({
        i: this.config.items.length+4,
        url: "https://grainger-engineering-library.github.io/gridvw/",
        title: "",
        x:0,
        y:0,
        w:1920,
        h:500,
        spawn: true
      })
    },
    componentURLUpdated(url,i) {
      this.config.items[i].url=url
    },
    updatePlaceholder: function(key) {
      this.config.gl[key].placeholder=this.config.gl[key].value.toString()
    }
  },
  mounted() {
    this.updatePlaceholder("colnum");
    this.updatePlaceholder("rowheight");
  },
  pushView: function() {
      axios.post("http:localhost:5000/views", {data: this.config})
  }
}
</script>

<style>
#app {
  height: 100vh
}

</style>
