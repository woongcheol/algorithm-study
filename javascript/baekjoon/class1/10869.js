// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/10869.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split(" ")
  .map((val) => parseInt(val));

// my solved : memory 9600kb, time 144ms
const solved = (inputData) => {
  const [numA, numB] = inputData;
  console.log(numA + numB);
  console.log(numA - numB);
  console.log(numA * numB);
  console.log(parseInt(numA / numB));
  console.log(numA % numB);
};

// checked solved
solved(inputData);
