// ( 데이터 입력부 )

// 1. 라이브러리 불러오기
const fs = require("fs"); // 내장 모듈

// 2. 파일 불러오기
const fileBuffer = fs.readFileSync("javascript/baekjoon/class1/1157.txt"); // 버퍼 객체로 바이너리 데이터를 반환, <Buffer ? ? ?>
const inputData = fileBuffer.toString().trim(); // 데이터 변환 전 String 객체로 사전 변환

// ( 알고리즘 입력부 )
const algotirthm = (inputData) => {
  // 1. 데이터 변환
  const transData = inputData.toLowerCase();

  // 2. 적용
  const map = new Map();

  for (letter of transData) {
    if (map.has(letter)) {
      map.set(letter, map.get(letter) + 1);
    } else {
      map.set(letter, 1);
    }
  }

  let maxFrequency = 0;
  let mostFrequecyLetter = "";

  for (const [letter, frequency] of map) {
    if (frequency > maxFrequency) {
      maxFrequency = frequency;
      mostFrequecyLetter = letter;
    } else if (frequency == maxFrequency) {
      mostFrequecyLetter = "?";
    } else {
      continue;
    }
  }

  // ( 데이터 출력부 )
  console.log(mostFrequecyLetter.toUpperCase());
};

algotirthm(inputData);
