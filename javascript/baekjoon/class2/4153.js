// 1. 데이터 입력부
// 1-1. 라이브러리 불러오기
const fs = require("fs");

// 1-2. 데이터 불러오기 : 텍스트 파일
const inputFile = fs.readFileSync("javascript/baekjoon/class2/4153.txt");

// 1-3. 데이터 준비 : String 객체 변환 및 공백제거
const inputData = inputFile.toString().trim();

// 2. 알고리즘 입력부
const algorithm = (inputData) => {
  // 2-1. 데이터 변환
  const transData = inputData
    .split("\n")
    .map((val) => val.split(" ").map(Number));

  // 2-2. 검증 : 직각 삼각형 여부
  for (item of transData) {
    const triangleArr = item;

    // 정렬 처리
    triangleArr.sort((a, b) => a - b);
    const [a, b, c] = triangleArr;

    // 종료 여부 검증
    if (a === 0 && b === 0 && c === 0) {
      break;
    }

    // 출력
    if (a * a + b * b == c * c) {
      console.log("right");
    } else {
      console.log("wrong");
    }
  }
};

algorithm(inputData);
