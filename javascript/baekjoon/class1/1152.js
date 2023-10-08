// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/1152.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData ? inputData.split(" ") : [];

// 알고리즘 적용
const solved = (transData) => {
  const wordCount = transData.length;

  // 답안 출력
  console.log(wordCount);
};

solved(transData);
