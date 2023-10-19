const fs = require("fs");

// // 입력 파일 경로 상수 정의
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/15829.txt";

// 알고리즘 입력 부
// 알파벳 수열 변환 함수
const transAlphaToNum = (alphaList) => {
  const initAsciiNum = 96;
  const numList = [];

  for (alpha of alphaList) {
    numList.push(alpha.charCodeAt() - initAsciiNum);
  }

  return numList;
};

// 수열 합계 처리 함수
const sumNumList = (numList) => {
  const modNum = 1234567891;
  const r = 31;
  let sum = 0;
  let nextR = 1;

  // Number.MIN_SAFE_INTEGER(9,007,199,254,740,991) 초과 시 오류 발생, 주기적으로 나머지 연산 필요
  for (num of numList) {
    sum = (sum + num * nextR) % modNum;
    nextR = (nextR * r) % modNum;
  }

  return sum;
};

// 입력 데이터,  변환 함수
const transformInputData = (inputData) => {
  return inputData.split("\n");
};

// 메인 함수 입력 부
const main = (inputData) => {
  // 입력 데이터 변환
  const [L, data] = transformInputData(inputData);

  // 알파벳 배열 -> 수열로 변환
  const numList = transAlphaToNum(data);

  // 수열 합계 처리
  const sumNum = sumNumList(numList);
  console.log(sumNum);
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
