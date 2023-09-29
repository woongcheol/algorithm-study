const fs = require("fs");
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2884.txt")
  .toString()
  .trim();

// 9340kb, 132ms
const solved = (inputData) => {
  let [H, M] = inputData.split(" ").map(Number);

  if (M < 45 && 0 < H) {
    M += 15;
    H -= 1;
  } else if (M < 45 && 0 == H) {
    M += 15;
    H = 23;
  } else {
    M -= 45;
  }

  console.log(H, M);
};

solved(inputData);
