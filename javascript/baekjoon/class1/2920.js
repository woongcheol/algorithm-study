// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2920.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData.split(" ").map(Number);

// 알고리즘 적용
const solved = (transData) => {
  const firstNum = transData[0];
  let result = "mixed";

  // ascending or mixed
  if (firstNum == 1) {
    for (let i = 0; i < 8; i++) {
      if (transData[i] !== i + 1) {
        result = "mixed";
        break;
      }
      result = "ascending";
    }

    // descending or mixed
  } else if (firstNum == 8) {
    for (let i = 0; i < 8; i++) {
      if (transData[i] !== 8 - i) {
        result = "mixed";
        break;
      }
      result = "descending";
    }
  }

  console.log(result);
};

solved(transData);
