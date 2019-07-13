<template>
  <div>
    <notifications></notifications>
    Redirecting...
  </div>
</template>

<script>
import axios from 'axios';

const appConfig = require('../../config.js');     // Auth keys and redirect
const boxSDK = require('box-node-sdk'); 
const querystring = require('querystring');   // Querystring stringifier


export default {
    // data() {
    //     return {
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
        // eslint-disable-next-line 
        console.log('client_id', appConfig.oauthClientId, 'client_secret', appConfig.oauthClientSecret);

        // Extract auth code
        const code = q.code;
        const csrf = q.state
        console.log('code', code, 'state', csrf);

        let payload = {
            grant_type: 'authorization_code',
            code: q.code,
            client_id: appConfig.oauthClientId,
            client_secret: appConfig.oauthClientSecret
        }

        let qs = querystring.stringify(payload)

        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
        
        axios.post('https://api.box.com/oauth2/token', qs, config)
        .then(response => {
            console.log(response);
            let data = response.data;
            let tokenInfo = {
                accessToken: data.access_token,
                refreshToken: data.refresh_token,
                accessTokenTTLMS: data.expires_in,
                acquiredAtMS: Date.now() 
            }
            console.log(tokenInfo);
            try {
                const client = sdk.getPersistentClient(tokenInfo);
                console.log(client);
                this.$notify({
                    message:
                    "Box client created",
                    icon: "add_alert",
                    horizontalAlign: "top",
                    verticalAlign: "right",
                    type: "success"
                });
            }
            catch(err) {
                console.log(err);
            }

        });

        /*
        * Validate that an object is a valid TokenInfo object
        * @param {Object} obj The object to validate
        * @returns {boolean} True if the passed in object is a valid TokenInfo object that
        *  has all the expected properties, false otherwise
        * @private

        function isObjectValidTokenInfo(obj) {
            return Boolean(obj &&
                obj.accessToken &&
                obj.refreshToken &&
                obj.accessTokenTTLMS &&
                obj.acquiredAtMS);
        }
        */

        // sdk.getTokensAuthorizationCodeGrant(code, function(err, tokenInfo) {
        //     try {
        //         const client = sdk.getPersistentClient(tokenInfo);
        //         console.log(client);
        //     }
        //     catch(err) {
        //         console.log(err);
        //     }
        // });

    }
}
</script>
