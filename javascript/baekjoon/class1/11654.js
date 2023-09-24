const fs = require("fs");

const inputData = fs.readFileSync("./javascript/baekjoon/class1/11654.txt");

const alphabet = inputData.toString().trim();

// 9336kb, 128ms
const solved = (alphabet) => alphabet.charCodeAt(0);

console.log(solved(alphabet));
