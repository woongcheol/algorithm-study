#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int *pointA = (int *)a;
    int *pointB = (int *)b;

    if (pointA[0] == pointB[0]) {
        return pointA[1] - pointB[1];
    }

    return pointA[0] - pointB[0];
}

int main(void) {
    freopen("11650.txt", "r", stdin);

    int N;

    scanf("%d", &N);

    // 2D 배열 선언 및 동적 할당
    int (*arr)[2] = malloc(sizeof(int[N][2]));

    for (int i = 0; i < N; i++) {
        int x, y;
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }

    qsort(arr, N, sizeof(arr[0]), compare);

    for (int i = 0; i < N; i++) {
        printf("%d %d\n", arr[i][0], arr[i][1]);
    }

    free(arr); // 할당된 메모리 해제

    return 0;
}
