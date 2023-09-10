// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./class1/1002.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split(" ")
  .map((value) => +value);

const [a, b] = inputData;

// my solved : memory 9604kb, time 124ms
const solved = a / b;

// checked solved
console.log(solved);
