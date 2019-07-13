<template>
  <!-- Material form login -->
  <form>
    <!-- <p class="h4 text-center mb-4">Sign in</p>
    <div class="grey-text">
      <mdb-input label="Your email" icon="envelope" type="email"/>
      <mdb-input label="Your password" icon="lock" type="password"/>
    </div> -->
    <div class="md-layout-item md-size-100 text-center">
      <md-button class="md-raised md-success" v-on:click="BoxOauth">Login</md-button>
    </div>
  </form>
  <!-- Material form login -->
</template>

<script>
const appConfig = require('../../config.js');     // Auth keys and redirect
const querystring = require('querystring');   // Querystring stringifier

export default {
    methods: {
        BoxOauth() {
            // Build Box auth object
            const payload = {
            'response_type': 'code',
            'client_id': appConfig.oauthClientId,
            'redirect_uri': appConfig.redirectURI,
            'state': 'GENERATED_TOKEN'
            };

            // Build redirect URI and redirect
            const qs = querystring.stringify(payload);
            const authEndpoint = `https://account.box.com/api/oauth2/authorize?${qs}`;
            window.location.href = authEndpoint;
        }
    }
    
}
</script>
<style>

</style>

