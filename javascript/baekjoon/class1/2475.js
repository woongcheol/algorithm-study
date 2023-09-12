// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2475.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split(" ")
  .map((value) => +value);

let sumNum = 0;

// my solved : memory 9328kb, time 136ms
const solved = (inputData) => {
  for (num of inputData) {
    sumNum += num * num;
  }

  console.log(sumNum % 10);
};

// checked solved
solved(inputData);
