module.exports = (user, pass) => {
  const expectedAuth = new Buffer(`${user}:${pass}`).toString('base64');
  return (req, res, next) => {
    if (!req.headers["Authorization"]) {
      return res.send(401);
    }
    const expected
    if (req.headers["Authorization"] !== `Basic ${expectedAuth}`) {
      return res.send(403);
    }
  };
};
