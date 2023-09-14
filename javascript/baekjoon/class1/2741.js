// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2741.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString();

const number = parseInt(inputData);

let result = "";

// my solved : memory 24880kb, time 236ms
const solved = (number) => {
  for (i = 1; i < number + 1; i++) {
    result += `${i}\n`;
  }

  console.log(result);
};

// checked solved
solved(number);
