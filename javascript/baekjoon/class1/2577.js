// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2577.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData.split("\n").map(Number);

// 알고리즘 적용
const solved = (transData) => {
  const result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

  const [A, B, C] = transData;

  const sum = A * B * C;

  const sumToString = sum.toString();

  for (num of sumToString) {
    result[num] += 1;
  }

  // 답안 출력
  for (num of result) console.log(num);
};

solved(transData);
