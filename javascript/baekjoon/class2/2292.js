const fs = require("fs");

// 입력 파일 경로 상수 정의
const FILE_PATH = "javascript/baekjoon/class2/2292.txt";

// 알고리즘 입력 부
// 벌집 반지름 크기 검증 함수
const findPentagonRadius = (num) => {
  let pentagonNumber = 1;
  let max = 1;

  while (max < num) {
    max += pentagonNumber * 6;
    pentagonNumber++;
  }

  return pentagonNumber;
};

// 입력 데이터, Int 변환 함수
const transformInputData = (inputData) => {
  return parseInt(inputData);
};

// 메인 함수 입력 부
const main = (inputData) => {
  // 입력 데이터 숫자로 변환
  const num = transformInputData(inputData);

  // 벌집 수 확인 및 결과 출력
  const radius = findPentagonRadius(num);
  console.log(radius);
};

try {
  // 입력 파일을 동기적으로 읽고 입력 데이터 준비
  const inputFile = fs.readFileSync(FILE_PATH);
  const inputData = inputFile.toString().trim();

  // 메인 함수 호출
  main(inputData);
} catch (err) {
  console.error("Error reading the input file:", err);
}
