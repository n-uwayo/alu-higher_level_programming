#!/usr/bin/node

const fl1 = process.argv[2];
const fl2 = process.argv[3];
const newfile = process.argv[4];
const fs = require('fs');
const dt1 = fs.readFileSync(fl1, (err, data) => {
  if (err) throw err;
  return (data);
});
const dt2 = fs.readFileSync(fl2, (err, data) => {
  if (err) throw err;
  return (data);
});
fs.appendFile(newfile, dt1, function (err) {
  if (err) throw err;
});
fs.appendFile(newfile, dt2, function (err) {
  if (err) throw err;
});
