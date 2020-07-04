const chai = require('chai');
const chaiHttp = require('chai-http');

const app = require('./app');

chai.use(chaiHttp);
const expect = chai.expect;

describe("test", () => {
  it("should work", (done) => {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(err).to.be.null;
        expect(res.status).to.equal(200);
        expect(res.body).to.deep.equal({ hello: 'world' });
        done();
      })
  });
});
