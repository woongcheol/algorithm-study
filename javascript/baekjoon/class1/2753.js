// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2753.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString();

const number = parseInt(inputData);

// my solved : memory 9348kb, time 140ms
const solved = (number) => {
  if (number % 4 == 0 && number % 100 !== 0) {
    console.log(1);
  } else if (number % 400 == 0) {
    console.log(1);
  } else {
    console.log(0);
  }
};

// checked solved
solved(number);
