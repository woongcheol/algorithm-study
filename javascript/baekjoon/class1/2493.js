const fs = require("fs");
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2493.txt")
  .toString()
  .trim();

// 9804kb, 132ms
const solved = (inputData) => {
  const num = parseInt(inputData);

  for (let i = num - 1; -1 < i; i--) {
    let stars = [];
    for (let j = 0; j < num; j++) {
      if (i <= j) {
        stars += "*";
      } else {
        stars += " ";
      }
    }
    console.log(stars);
  }
};

solved(inputData);
