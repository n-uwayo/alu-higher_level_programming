#!/usr/bin/node

function add (num1, num2) {
  console.log(num1 + num2);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
