const fs = require("fs");

// 입력 파일 경로를 상수로 정의
const FILE_PATH = "javascript/baekjoon/class2/4153.txt";

// 삼각형 종류 문자열 상수 정의
const RIGHT_TRIANGLE = "right";
const WRONG_TRIANGLE = "wrong";

// 직각삼각형 여부를 판단하는 함수
const isRightTriangle = (a, b, c) => {
  // 세 변을 정렬
  const sortedSides = [a, b, c].sort((x, y) => x - y);
  const [sideA, sideB, sideC] = sortedSides;

  // 피타고라스 정리를 사용하여 직각삼각형 여부 판단
  return sideA * sideA + sideB * sideB === sideC * sideC;
};

// 삼각형을 분류하고 결과를 출력하는 함수
const classifyTriangles = (triangles) => {
  triangles.forEach(([a, b, c]) => {
    if (a === 0 && b === 0 && c === 0) {
      // 세 변이 모두 0이면 종료
      return;
    }

    // 직각삼각형 여부에 따라 결과 출력
    const result = isRightTriangle(a, b, c) ? RIGHT_TRIANGLE : WRONG_TRIANGLE;
    console.log(result);
  });
};

// 입력 데이터를 변환하는 함수
const transformInputData = (inputData) => {
  return inputData.split("\n").map((val) => val.split(" ").map(Number));
};

// 메인 함수
const main = (inputData) => {
  // 입력 데이터를 삼각형 배열로 변환
  const triangles = transformInputData(inputData);

  // 삼각형 분류 및 결과 출력
  classifyTriangles(triangles);
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
