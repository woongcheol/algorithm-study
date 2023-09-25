const fs = require("fs");

const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/27866.txt")
  .toString()
  .trim()
  .split("\n");

// 9324kb, 120ms
const solved = (inputData) => {
  let [word, num] = inputData;
  num = parseInt(num);

  console.log(word[num - 1]);
};

solved(inputData);
