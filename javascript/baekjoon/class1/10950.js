const fs = require("fs");

const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/10950.txt")
  .toString()
  .split("\n")
  .map((val) => val.split(" ").map(Number));

// my solved : memory 9604kb, time 152ms
const solved = (inputData) => {
  const testCaseNum = inputData[0][0];

  for (let t = 1; t < testCaseNum + 1; t++) {
    let num = 0;

    for (tc of inputData[t]) {
      num += tc;
    }

    console.log(num);
  }
};

solved(inputData);
