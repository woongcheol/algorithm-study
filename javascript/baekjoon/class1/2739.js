// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2739.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split(" ")
  .map((value) => +value);

// my solved : memory 9352kb, time 120ms
const solved = (inputData) => {
  for (i = 1; i < 10; i++) {
    console.log(`${inputData} * ${i} = ${inputData * i} `);
  }
};

// checked solved
solved(inputData);
