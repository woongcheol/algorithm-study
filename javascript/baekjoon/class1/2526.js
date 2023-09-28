const fs = require("fs");
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2526.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

// 9332kb, 120ms
const solved = (inputData) => {
  let maxIndex,
    max = 0;

  for (index in inputData) {
    if (max < inputData[index]) {
      maxIndex = index;
      max = inputData[index];
    }
  }

  console.log(max);
  console.log(+maxIndex + 1);
};

solved(inputData);
