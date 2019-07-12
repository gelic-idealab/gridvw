<template>
    <div>Redirecting...</div>
</template>

<script>
import axios from 'axios';

const querystring = require('querystring');   // Querystring stringifier
const appConfig = require('../../config.js');     // Auth keys and redirect
const boxSDK = require('box-node-sdk'); 

export default {
    // data() {
    //     return{
    //         tokenInfo: {
    //         accessToken: 'nvKMskt9VLDBpnYAvFZ5WKh2QpDallUA',
    //         refreshToken: '',
    //         acquiredAtMS: 0,
    //         accessTokenTTLMS: 0
    //         }
    //     }
    // },
    created() {
        let q = this.$route.query;

        // Create a new Box SDK instance
        const sdk = new boxSDK({
            clientID: appConfig.oauthClientId,
            clientSecret: appConfig.oauthClientSecret
        });
        
        // Extract auth code
        const auth_code = q.code;
        // console.log(code);
        
        const data = {
            grant_type: 'authorization_code',
            code: auth_code,
            client_id: appConfig.oauthClientId,
            client_secret: appConfig.oauthClientSecret
        };

        const qs = querystring.stringify(data);

        // Exchange code for access token
        sdk.getTokensAuthorizationCodeGrant(auth_code, null)
        .then(tokenInfo => {
            const client = sdk.getPersistentClient(tokenInfo);
            console.log(client);
        });

        // axios.post(`https://api.box.com/oauth2/token?${qs}`)
        // .then(response => console.log(response))
    }
}
</script>
