// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/10818.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData
  .split("\n")
  .map((val) => val.split(" ").map(Number));

// 알고리즘 적용
const solved = (transData) => {
  // 데이터 분리
  const [N] = transData[0];
  const number = transData[1];

  // 초깃값 적용
  let max = number[0];
  let min = number[0];

  for (let i = 0; i < N; i++) {
    if (max < number[i]) {
      max = number[i];
    } else if (min > number[i]) {
      min = number[i];
    }
  }

  console.log(min, max);
};

solved(transData);
