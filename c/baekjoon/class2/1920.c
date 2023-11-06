#include <stdio.h>
#include <stdlib.h>

/* 복기
- qsort와 이진 탐색 알고리즘을 적용하여 풀이함.
- 이진 탐색 시, first와 last 그리고 인덱스를 통해 탐색을 실시하였음. 이때 대소 비교에 따라 index를 제외한 수를 first와 last에 넣어줄 것
- 에러 발생 : 다음과 같은 데이터가 입력될 경우 qsort 시 오름차순이 적용되지 않는 현상 발생
    4
    2147483647 -5 -8 -11
    -> [2147483647, -5, -8, -11]
- 위의 오류는 compare 함수에서 return시 a-b 형태로 반환하는 것으로 인해 발생하는 문제였음. 이는 위와 같은 데이터에서 최대값을 넘어가므로 오류가 발생하는 것으로
  이를 해결하기 위해 대소 비교를 통해 1, 0, -1을 반환하는 것으로 수정해야함.
*/

// 이진 탐색
int binarySearchRecursive(int *arr, int first, int last, int num) {
    if (first <= last) {
        int index = (first + last) / 2;
        if (arr[index] == num) {
            return 1;
        } else if (arr[index] < num) {
            return binarySearchRecursive(arr, index + 1, last, num);
        } else {
            return binarySearchRecursive(arr, first, index - 1, num);
        }
    }
    return 0;
}

// 정렬
int compare(const void *a, const void *b) {
    if (*(int *)a > *(int *)b) {
        return 1;
    } else {
        return -1;
    }
}

int main(void) {
    int N;

    freopen("1920.txt", "r", stdin);
    scanf("%d", &N);

    // 배열 초기화 및 정렬
    int arr[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);

    // 이진 탐색
    int M;
    scanf("%d", &M);

    for (int i = 0; i < M; i++) {
        int num;
        int result;
        scanf("%d", &num);
        result = binarySearchRecursive(arr, 0, N - 1, num);
        printf("%d\n", result);
    }

    return 0;
}
