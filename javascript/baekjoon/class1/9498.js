// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/9498.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString();

const number = parseInt(inputData);

// my solved : memory 9348kb, time 140ms
const solved = (number) => {
  if (number >= 90) {
    console.log("A");
  } else if (number >= 80) {
    console.log("B");
  } else if (number >= 70) {
    console.log("C");
  } else if (number >= 60) {
    console.log("D");
  } else {
    console.log("F");
  }
};

// checked solved
solved(number);
