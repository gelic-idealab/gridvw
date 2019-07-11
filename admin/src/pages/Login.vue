<template>
  <!-- Material form login -->
  <form>
    <!-- <p class="h4 text-center mb-4">Sign in</p>
    <div class="grey-text">
      <mdb-input label="Your email" icon="envelope" type="email"/>
      <mdb-input label="Your password" icon="lock" type="password"/>
    </div> -->
    <div class="text-center">
      <mdb-btn v-on:click="oAuth">Login</mdb-btn>
    </div>
  </form>
  <!-- Material form login -->
</template>

<script>
const appConfig = require('../../config.js');     // Auth keys and redirect
const boxSDK = require('box-node-sdk');       // Box SDK
const querystring = require('querystring');   // Querystring stringifier
export default {
    methods: {
        oAuth() {
            // Build Box auth object
            const payload = {
            'response_type': 'code',
            'client_id': appConfig.oauthClientId,
            'redirect_uri': appConfig.redirectURI
            };

            // Build redirect URI and redirect
            const qs = querystring.stringify(payload);
            const authEndpoint = `https://account.box.com/api/oauth2/authorize?${qs}`;
            window.location.href = authEndpoint;
        }
    }
    
}
</script>
