// 파일 시스템 모듈 불러오기
const fs = require("fs");

// 입력 파일 경로 설정. (리눅스 환경에서는 표준 입력 사용)
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/2609.txt";

// 최대 공약수(GCD)를 계산하는 재귀 함수
function calculateGCD(a, b) {
  if (b === 0) {
    return a;
  }
  return calculateGCD(b, a % b);
}

// 주어진 숫자 배열의 최대 공약수(GCD) 계산 함수
function findGCD(arr) {
  const gcd = calculateGCD(arr[0], arr[1]);

  return gcd;
}

// 주어진 숫자 배열의 최소 공배수(LCM) 계산 함수
function findLCM(arr) {
  let lcm = 1;

  for (let num of arr) {
    lcm = (lcm * num) / calculateGCD(lcm, num);
  }
  return lcm;
}

// 메인 함수. 입력 데이터 처리 및 결과 출력
function main(inputData) {
  // 입력 데이터를 공백으로 분리하고 숫자로 변환
  const numbers = inputData.split(" ").map(Number);

  // 최대 공약수 및 공배수 계산
  const gcd = findGCD(numbers); // 최대 공약수(GCD) 계산
  const lcm = findLCM(numbers); // 최소 공배수(LCM) 계산

  console.log(gcd); // 최대 공약수(GCD) 출력
  console.log(lcm); // 최소 공배수(LCM) 출력
}

try {
  // 입력 파일을 동기적으로 읽고 문자열로 변환한 뒤 양 끝의 공백 제거
  const inputFile = fs.readFileSync(FILE_PATH, "utf8").trim();
  main(inputFile); // 메인 함수 호출 및 결과 출력
} catch (err) {
  console.error("Error:", err.message); // 에러 발생 시 에러 메시지 출력
}
