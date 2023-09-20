const fs = require("fs");

const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/10951.txt")
  .toString()
  .trim()
  .split("\n");

// my solved : memory 9508kb, time 128ms
const solved = (inputData) => {
  for (let tc = 0; tc < inputData.length; tc++) {
    const [a, b] = inputData[tc].split(" ").map(Number);
    console.log(a + b);
  }
};

solved(inputData);
