// 데이터 입력, 모듈 import
const fs = require("fs");

// 데이터 입력, 문자열 처리
const inputData = fs
  .readFileSync("javascript/baekjoon/class1/10250.txt")
  .toString()
  .trim();

// 데이터 변환, 입력 조건 적용
const transData = inputData
  .split("\n")
  .map((val) => val.split(" ").map(Number));

// 알고리즘 적용
const solved = (transData) => {
  // 데이터 분리
  const [T] = transData[0];

  // 반복문 적용
  for (let i = 1; i <= T; i++) {
    const [H, W, N] = transData[i];

    // 층수 적용, 나머지가 있을 시 나머지 출력
    const h = N % H ? N % H : H;

    // 호수 적용, 나머지가 있을 시 몫 출력
    const w = N % H ? parseInt(N / H) + 1 : N / H;

    // 객실이 10호 미만 및 이상일 경우 처리
    if (w >= 10) {
      console.log(`${h}${w}`);
    } else {
      console.log(`${h}0${w}`);
    }
  }
};

solved(transData);
