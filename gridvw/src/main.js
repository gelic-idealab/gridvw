import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'

// import 'materialize-css/dist/js/materialize.min.js' // Ensure you are using css-loader
// import 'materialize-css/dist/css/materialize.min.css' // Ensure you are using css-loader
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import 'vuetify/dist/vuetify.min.js' // Ensure you are using css-loader


Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
