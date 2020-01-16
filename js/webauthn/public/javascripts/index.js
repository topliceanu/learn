// Step zero in the webauthn flow.
// @param {String} email
// @return {Object} ret
// @return {Uint8Array} ret.challenge - byte array be signed by the client.
// @return {Object} ret.user - user information
// @return {Uint8Array} ret.user.id - unique id encoded as a byte array.
// @return {String} ret.user.name - the user's email.
// @return {Object} ret.rp - information about the server (or relaying party).
const requestRegistration = async (email) => {
  const res = await fetch('/users/registration/request', {
    method: 'post',
    cache: 'no-cache',
    headers: {
      'Content-type': 'application/json',
      'Accept': 'application/json',
    },
    // TODO server has to do some validation of the payload.
    body: JSON.stringify({email})
  });
  return res.json();
}

// @param {Uint8Array} challengeRaw
// @return {Uint8Array} signed challenge
const signChallenge = async (challengeRaw, keyId) => {
  // TODO, see https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/sign
  return window.crypto.subtle.sign();
}

const onSubmit = () => {
  const email = document.getElementById('email').value;
  const serverOptions = await requestRegistration(email);
  const credentialsCreationOptions = Object.assign({}, serverOptions, {
    // I assume the client decides what type of asymetric key to generate on registration.
    pubKeyCredentials: [{
      type: 'public-key', alg: -7, // -7 stands for	'ECDSA w/ SHA-256'
    }],
    attestation: 'direct', // what options do we have here? should this be decided by the client?
    authenticatorSelection: {
      authenticatorAttachment: 'cross-platform', // what options do we have here? should this be on the server?
    },
    timeout: 60000, // timeout for the user to confirm authentication. Q: should the server have a similar timeout? Q: should it be related to this timeout?
  })
  const credential = await navigator.credentials.create(credentialsCreationOptions); // Type PublicKeyCredential
  const await = completeRegistration({
    signedChallenge: sign(serverOptions.challenge, credential.id),
    publicKey: {
      id: credential.id,
      type: credential.type,
      key: credential.
  })
}



(async () => {
  // TODO
})();



/*
const toUint8Array = (str) => {
  return Uint8Array.from(str, c => c.charCodeAt(0));
};

// [This page](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialCreationOptions) has more descriptions.
const publicKeyCredentailsOptions = {
  // Should be used to compute a signature on the client-side
  challenge: Uint8Array.from(toUint8Array),
  rp: { // relaying party - organization which is
    name: 'Pusher',
    //id: 'dev.me', // must be a subset of the current domain
  },
  user: {
    // Some random id but has to be ArrayBuffer.
    id: toUint8Array(Math.random().toString(36).substring(2, 10)),
    name: 'Alexandru Topliceanu',
    displayName: 'dru',
  },
  // this is a required field.
  pubKeyCredParams: [
    {alg: -7, type: 'public-key'}, // -7 stands for	'ECDSA w/ SHA-256'
  ],
  authenticatorSelection: {
    authenticatorAttachment: 'cross-platform',
  },
  timeout: 60000, // timeout for the user to confirm authentication
  attestation: 'direct',
};

(async () => {
  // The [navigator credentials object](https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer)
  const credential = await navigator.credentials.create({
    // The [PublicKeyCredentialsCreationOptions](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialCreationOptions)
    publicKey: publicKeyCredentailsOptions,
  });
  console.log(credential);
})();
*/
