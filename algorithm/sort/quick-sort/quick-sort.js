function quicksort(q) {
  if (q.length <= 1) {
    return q;
  }

  const pivot = q[0];

  const less = new Array();
  for (let i = 1; i < q.length; i++) {
    if (q[i] < pivot) {
      less.push(q[i]);
    }
  }

  const greater = new Array();
  for (let i = 1; i < q.length; i++) {
    if (q[i] >= pivot) {
      greater.push(q[i]);
    }
  }

  const qResult = quicksort(less) + [pivot] + quicksort(greater);

  return qResult;
}

const myArray = [5, 2, 9, 3, 6, 1];
const sortedArray = quicksort(myArray);
console.log(sortedArray);
