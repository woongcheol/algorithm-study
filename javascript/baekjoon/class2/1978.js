const fs = require("fs");

// 입력 파일 경로를 상수로 정의
const FILE_PATH = "javascript/baekjoon/class2/1978.txt";

// 입력 데이터를 변환하는 함수
const transformInputData = (inputData) => {
  return inputData.split("\n").map((val) => val.split(" ").map(Number));
};

// 소수 검증 함수
const isPrime = (num) => {
  if (num < 2) {
    return false;
  }

  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
};

// 메인 함수
const main = (inputData) => {
  // 입력 데이터를 소수 개수 및 소수 배열로 변환
  const [n, nums] = transformInputData(inputData);

  // 결과 입력 변수 선언 및 초기화
  let result = 0;

  // 알고리즘 적용
  for (num of nums) {
    if (isPrime(num)) {
      result += 1;
    }
  }

  // 출력
  console.log(result);
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
