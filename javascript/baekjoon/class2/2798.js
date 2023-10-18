const { log } = require("console");
const fs = require("fs");

// 입력 파일 경로 상수 정의
const FILE_PATH = "javascript/baekjoon/class2/2798.txt";

// 알고리즘 입력 부
// 카드 합계 최댓값 검증 함수
const findMaxCardSum = (N, M, cards) => {
  // - 카드 배열 정렬 : 오름차순
  cards.sort((a, b) => a - b);

  // - 최대 합 초기값 및 합계 설정
  let max = 0;
  let tempSum = 0;

  // - 카드 합계 검증
  for (let i = 0; i < N - 2; i++) {
    const a = cards[i];

    if (M < a) {
      return max;
    }

    for (let j = i + 1; j < N - 1; j++) {
      const b = cards[j];

      if (M < a + b) {
        return max;
      }

      for (let k = j + 1; k < N; k++) {
        const c = cards[k];

        tempSum = a + b + c;

        if (M < tempSum) {
          break;
        } else if (M === tempSum) {
          return tempSum;
        } else if (max < tempSum) {
          max = tempSum;
        }
      }
    }
  }

  return max;
};

// 입력 데이터, 변환 함수
const transformInputData = (inputData) => {
  return inputData.split("\n").map((value) => value.split(" ").map(Number));
};

// 메인 함수 입력 부
const main = (inputData) => {
  // 입력 데이터 변환
  const [condition, cards] = transformInputData(inputData);
  const [N, M] = condition;

  const resultMax = findMaxCardSum(N, M, cards);
  console.log(resultMax);
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
