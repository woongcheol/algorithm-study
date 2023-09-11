// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/1330.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split(" ")
  .map((value) => +value);

const [a, b] = inputData;

// my solved : memory 9336kb, time 116ms
const solved = (a, b) => {
  if (a > b) {
    return ">";
  } else if (a < b) {
    return "<";
  } else {
    return "==";
  }
};

// checked solved
console.log(solved(a, b));
