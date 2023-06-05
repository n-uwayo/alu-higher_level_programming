#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDicterory = {};
for (const j in valsUniq) {
  const lists = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      lists.unshift(totalist[k][0]);
    }
  }
  newDicterory[valsUniq[j]] = lists;
}
console.log(newDicterory);
