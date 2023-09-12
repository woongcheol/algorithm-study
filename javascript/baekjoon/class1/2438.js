// import the common library
const fs = require("fs");

// import the input data
const inputData = fs
  .readFileSync("./javascript/baekjoon/class1/2438.txt") // If 'submit', change the argument of readFileSync to "/dev/stdin"
  .toString();

const num = parseInt(inputData);

// my solved : memory 12656kb, time 452ms
const solved = (num) => {
  for (var i = 0; i < num; i++) {
    for (var j = 0; j < i + 1; j++) {
      process.stdout.write("*");
    }
    console.log();
  }
};

// checked solved
solved(num);
