function quicksort(q) {
  if (q.length <= 1) {
    return q;
  }

  const pivot = q[0];
  const less = [];
  const greater = [];

  for (let i = 1; i < q.length; i++) {
    if (q[i] < pivot) {
      less.push(q[i]);
    } else {
      greater.push(q[i]);
    }
  }

  // 문자열로 변환할 때
  // const qResult = quicksort(less) + [pivot] + quicksort(greater);

  // 배열로 생성
  const qResult = quicksort(less).concat([pivot], quicksort(greater));

  return qResult;
}

const myArray = [9, 5, 2, 9, 3, 6, 3, 1];
const sortedArray = quicksort(myArray);
console.log(sortedArray);
