// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2557.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString();

// my solved : memory 9328kb, time 136ms
const solved = (inputData) => {
  console.log("Hello World!");
};

// checked solved
solved(inputData);
