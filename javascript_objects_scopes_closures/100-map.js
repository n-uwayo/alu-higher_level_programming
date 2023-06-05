#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
const TheNewList = list.map(function (x, idx) {
  return (x * idx);
});
console.log(TheNewList);
