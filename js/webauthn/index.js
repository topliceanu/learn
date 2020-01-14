const toUint8Array = (str) => {
  return Uint8Array.from(str, c => c.charCodeAt(0));
};

// [This page](https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialCreationOptions) has more descriptions.
const publicKeyCredentailsOptions = {
  // Should be used to compute a signature on the client-side
  challenge: Uint8Array.from(toUint8Array),
  rp: { // relaying party - organization which is
    name: "Pusher",
    //id: "dev.me", // must be a subset of the current domain
  },
  user: {
    // Some random id but has to be ArrayBuffer.
    id: toUint8Array(Math.random().toString(36).substring(2, 10)),
    name: "Alexandru Topliceanu",
    displayName: "dru",
  },
  // this is a required field.
  pubKeyCredParams: [
    {alg: -7, type: "public-key"}, // -7 stands for	"ECDSA w/ SHA-256"
  ],
  authenticatorSelection: {
    authenticatorAttachment: "cross-platform",
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
