const crypto = require('crypto');

const express = require('express');

const router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/login', function(req, res, next) {
  res.render('login', { title: 'Login' });
});

router.get('/register', function(req, res, next) {
  res.render('register', { title: 'Register' });
});

/*
// @param {String} req.body.email - it will use it to fetch the id.
router.get('/registration/request', (req, res, next) => {
  const challenge = crypto.randomBytes(256);

  return res.status(200).json({
    challenge: challenge.toString('base64'),
    rp: {
      name: "test",
    },
    user: {
      id: 1,
      name: "name",
      displayName: "displayName",
    },
  });
});

module.exports = router;
*/

/*
router.post('/registration/request', (req, res, next) => {
  const { email, username } = req.body;
  const challengeBuf = crypto.randomBytes(256);
  const newSignup = {
    id: uuidv4(),
    email: email,
    challenge: challengeBuf,
    ts: Date.now(),
  };
  req.session.newSignup = newSignup;
  // The type of the returned object is https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialCreationOptions
  res.status(200).json({
    challenge: challengeBuf,
    user: {
      id: Buffer.from(newSignup.id), // Q: are these buffers decoded as Uint8Arrays on the client side?!
      displayName: username,
      name: email,
    },
    rp: {
      id: 'localhost', // url of this server
      name: 'Web Authentication server',
    },
    // The server decides what the method the client needs to use the sign the challenge.
    pubKeyCredentials: [{
      type: 'public-key', // it's the only option supported as of writing.
      alg: -7, // -7 stands for	'ECDSA w/ SHA-256'
    }],
    timestamp: 1 * 60 * 1000, // one minute in milliseconds
    // excludeCredentials: ... - a list of credentials that the client should not use.
    // authenticatorSelection: ... - chose which types of authenticators the client is allowed to use.
    // presumably, the server can use this to kick-out the user with a specific credential
    attestation: 'none'  // see https://developer.mozilla.org/en-US/docs/Web/API/PublicKeyCredentialCreationOptions/attestation
  });
});

*/
