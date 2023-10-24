// 파일 시스템 모듈 불러오기
const fs = require("fs");

// 입력 파일 경로 설정. (리눅스 환경에서는 표준 입력 사용)
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/2869.txt";

// 달팽이 막대 이동 기간 구하기
const findDay = (A, B, V) => {
  // 경과일
  const day = (V - B) / (A - B);

  return day;
};

// 메인 함수
function main(inputData) {
  // 입력 데이터 분리 및 숫자 변환
  const [A, B, V] = inputData.split(" ").map(Number);

  // day 확인
  const day = findDay(A, B, V);

  // day 소수점 반올림 처리
  const dayToInt = parseInt(day); // Math.ceil도 가능

  // 반올림 됐을 경우 +1 처리
  if (day > dayToInt) {
    console.log(dayToInt + 1);
  } else {
    console.log(day);
  }
}

try {
  // 입력 파일을 동기적으로 읽고 문자열로 변환한 뒤 양 끝의 공백 제거
  const inputFile = fs.readFileSync(FILE_PATH, "utf8").trim();
  main(inputFile); // 메인 함수 호출 및 결과 출력
} catch (err) {
  console.error("Error:", err.message); // 에러 발생 시 에러 메시지 출력
}
