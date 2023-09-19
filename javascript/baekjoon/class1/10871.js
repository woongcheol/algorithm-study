// import the common library
const fs = require("fs");

// import the input data
const inputData = require("fs")
  .readFileSync("./javascript/baekjoon/class1/10871.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

// my solved : memory 9600kb, time 144ms
const solved = (inputData) => {
  let [N, X] = inputData.shift();
  let A = inputData[0];
  let result = "";
  for (num of A) {
    if (num < X) {
      result += `${num} `;
    }
  }

  console.log(result);
};

// checked solved
solved(inputData);
