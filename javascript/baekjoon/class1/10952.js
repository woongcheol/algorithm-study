const fs = require("fs");

// 9596kb, 136ms
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/10952.txt")
  .toString()
  .trim()
  .split("\n")
  .map((val) => val.split(" ").map(Number));

for (numSet of inputData) {
  let [a, b] = numSet;
  if (a + b == 0) {
    return;
  }
  console.log(a + b);
}
