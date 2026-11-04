
const test = require('node:test');
const assert = require('node:assert/strict');
const { sumar } = require('../app');

test('sumar numeros positivos', () => {
  assert.equal(sumar(2, 3), 5);
});
