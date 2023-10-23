// 파일 시스템 모듈 불러오기
const fs = require("fs");

// 입력 파일 경로 설정. (리눅스 환경에서는 표준 입력 사용)
const FILE_PATH =
  process.platform === "linux"
    ? "/dev/stdin"
    : "javascript/baekjoon/class2/2775.txt";

// 호실별 거주 인원 수 확인
const updateResident = (list, k, c) => {
  // 0 미만일 경우 종료 처리
  if (k - 1 < 0 || c < 1) {
    return;
  }

  // 오름차순 업데이트
  let tempSum = 1;

  for (let i = 2; i < c + 1; i++) {
    // 아래층 호수의 값이 없을 경우 재귀함수 처리
    if (list[k - 1][i] == 0) {
      updateResident(list, k - 1, i);
    }

    // 이전 호수의 값이 있을 경우 합산 처리
    tempSum += list[k - 1][i];
  }
  list[k][c] = tempSum;

  return;
};

// 메인 함수
function main(inputData) {
  // 입력 데이터 분리 및 숫자 변환
  const [t, ...tc] = inputData.split("\n").map(Number);

  const list = [];

  // 배열 초기화
  list.push([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]);

  // 테스트 케이스별 반복문 순회
  for (let i = 0; i < t * 2; i = i + 2) {
    const k = tc[i];
    const n = tc[i + 1];

    // 해당 층의 리스트가 비어있을 경우 추가 업데이트
    for (let j = 1; j <= tc[i]; j++)
      if (list[j] == undefined) {
        list.push([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
      }

    // 재귀함수 호출 및 결과 출력
    updateResident(list, k, n);
    console.log(list[k][n]);
  }
}

try {
  // 입력 파일을 동기적으로 읽고 문자열로 변환한 뒤 양 끝의 공백 제거
  const inputFile = fs.readFileSync(FILE_PATH, "utf8").trim();
  main(inputFile); // 메인 함수 호출 및 결과 출력
} catch (err) {
  console.error("Error:", err.message); // 에러 발생 시 에러 메시지 출력
}
