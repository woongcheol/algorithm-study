const fs = require("fs");

// 9340kb, 144ms
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/10998.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [a, b] = inputData;

console.log(a * b);
