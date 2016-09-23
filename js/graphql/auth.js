const crypto = require('crypto');

module.exports = (user, pass) => {
  const hash = crypto.createHash('md5');
  hash.update(`${user}:${pass}`);
  const expectedAuth = hash.digest('hex');

  return (req, res, next) => {
    /*
    if (!req.headers["authorization"]) {
        return res.sendStatus(401);
    }
    if (req.headers["authorization"] !== `Basic ${expectedAuth}`) {
      return res.sendStatus(403);
    }
    */
    next();
  };
};
