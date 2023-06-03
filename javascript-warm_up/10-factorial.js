#!/usr/bin/node
function factorial (number) {
    if (isNaN(number)) {
      return 1;
    }
    else if (n === 0) {
        return 1;
    }
    else{
        return num * factorial(number - 1);
    }   
  }
  console.log(factorial(parseInt(process.argv[2])));
