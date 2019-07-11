<template>
    <div>Redirecting...</div>
</template>

<script>

const appConfig = require('../../config.js');     // Auth keys and redirect
const boxSDK = require('box-node-sdk'); 

export default {
    mounted () {
        let q = this.$route.query;

        // Create a new Box SDK instance
        const sdk = new boxSDK({
            clientID: appConfig.oauthClientId,
            clientSecret: appConfig.oauthClientSecret
        });

        // Extract auth code
        const code = q.code;

        // Exchange code for access token
        sdk.getTokensAuthorizationCodeGrant(code, null, function(err, tokenInfo) {
            const client = sdk.getPersistentClient(tokenInfo);

            console.log(client);
        });
        
    }
    
}
</script>
