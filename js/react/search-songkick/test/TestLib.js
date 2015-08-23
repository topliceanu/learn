var chai = require('chai');

var access = require('../app/lib/access');


describe('lib', function () {
    describe('.access()', function () {
        it('should correctly return the nested value', function () {
            var subject = {a: {b: { c: { d: true}}}};

            var actual = access(subject, 'a.b.c.d');
            chai.assert.equal(actual, true, 'should access nested value');

            var actual = access(subject, 'a.b.c.e');
            chai.assert.equal(actual, undefined, 'no nested value found');
        });
    });
});
