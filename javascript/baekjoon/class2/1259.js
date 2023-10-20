const fs = require("fs");

// // 입력 파일 경로 상수 정의
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/1259.txt";

// 알고리즘 입력 부
// 펠린드롬수 검증
const isPalindrome = (num) => {
  const str = num.toString();
  const reversedStr = str.split("").reverse().join("");
  return str === reversedStr;
};

// 입력 데이터, 변환 함수
const transformInputData = (inputData) => {
  return inputData.split("\n").map(Number);
};

// 메인 함수 입력 부
const main = (inputData) => {
  const numbers = transformInputData(inputData);

  for (const number of numbers) {
    if (number === 0) break;
    console.log(isPalindrome(number) ? "yes" : "no");
  }
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
