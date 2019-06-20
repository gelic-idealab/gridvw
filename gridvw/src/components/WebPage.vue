<template>
  <div class="web-page">
    <!-- <div class="container"> -->
      <!-- <div class="row">
        <input v-model="localUrl" placeholder="url" id="url" type="text" v-on:change="onUpdate">
        <label for="url">Component URL</label>
      </div> -->
      <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <v-card-text>
            <v-text-field v-model="url" label="Component URL"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat color="primary" v-on:click="onUpdate">Submit</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-btn @click="dialog = !dialog" fab absolute small bottom left hover color="blue" ><v-icon color="white">edit</v-icon></v-btn>
      <div class="row">
        <embed v-bind:src="localUrl" frameborder=0 width="100%" :height="h"/>
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
      localUrl: this.url,
      dialog: false
    }
  },
  methods: {
      onUpdate() {
        this.dialog = false;
        this.localUrl=this.url
        this.$emit('update:url', this.localUrl);
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
