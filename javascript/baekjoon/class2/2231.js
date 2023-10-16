const fs = require("fs");

// 입력 파일 경로 상수 정의
const FILE_PATH = "javascript/baekjoon/class2/2231.txt";

// 알고리즘 입력 부
// 주어진 수의 생성자를 찾아 출력
const findConstructor = (num) => {
  // - 생성자 초기화
  let result = 1;

  // - 생성자 탐색
  while (result <= num) {
    // - 임시 분해합 초기화
    let temp = 0;

    // - 본인 자릿수 계산
    temp += result;

    // - 각 자릿수 계산
    const individualNumList = result.toString().split("").map(Number);

    for (let i of individualNumList) {
      temp += i;
    }

    // - 분해합이 맞을 경우 생성자 출력
    if (num == temp) {
      console.log(result);
      break;
    }
    // - 분해합이 없을 경우 "0" 출력
    if (num <= result) {
      console.log(0);
    }

    // - 생성자 업데이트
    result++;
  }
};

// 2. 입력 데이터를 변환하는 함수
const transformInputData = (inputData) => {
  return parseInt(inputData);
};

// 메인 함수 입력 부
const main = (inputData) => {
  // 입력 데이터 숫자로 변환
  const num = transformInputData(inputData);

  // 생성자 탐색 및 결과 출력
  findConstructor(num);
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
