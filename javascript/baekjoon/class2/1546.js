// 파일 시스템 모듈 불러오기
const fs = require("fs");

// 입력 파일 경로 설정. (리눅스 환경에서는 표준 입력 사용)
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/1546.txt";

// 메인 함수. 입력 데이터 처리 및 결과 출력
function main(inputData) {
  const [[N], scoreList] = inputData
    .split("\n")
    .map((val) => val.split(" ").map(Number));

  // 최고 점수 확인
  const M = Math.max(...scoreList);

  // 점수 변환
  const transScoreList = [];

  for (score of scoreList) {
    transScoreList.push((score / M) * 100);
  }

  // 점수 평균
  let sum = 0;

  for (transScore of transScoreList) {
    sum += transScore;
  }

  console.log(sum / N);
}

try {
  // 입력 파일을 동기적으로 읽고 문자열로 변환한 뒤 양 끝의 공백 제거
  const inputFile = fs.readFileSync(FILE_PATH, "utf8").trim();
  main(inputFile); // 메인 함수 호출 및 결과 출력
} catch (err) {
  console.error("Error:", err.message); // 에러 발생 시 에러 메시지 출력
}
