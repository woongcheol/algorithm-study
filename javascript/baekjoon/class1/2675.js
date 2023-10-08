// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/2675.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData.split("\n").map((val) => val.split(" "));

// 알고리즘 적용
const solved = (transData) => {
  console.log(transData);

  // 테스트 케이스 수
  const [T] = transData[0];

  // 테스트 케이스 풀이
  for (let i = 1; i <= parseInt(T); i++) {
    let result = [];
    const [R, S] = transData[i];

    for (letter of S) {
      for (let i = 0; i < parseInt(R); i++) {
        result += letter;
      }
    }

    // 답안 출력
    console.log(result);
  }
};

solved(transData);
