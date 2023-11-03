#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
    int *pointA = (int *)a;
    int *pointB = (int *)b;

    if (pointA[1] > pointB[1]) {
        return pointA[1] - pointB[1];
    } else if (pointA[1] == pointB[1]) {
        return pointA[0] - pointB[0];
    } 

    return pointA[1] - pointB[1];

}

int main(void) {

    freopen("11651.txt", "r", stdin);

    int N;

    scanf("%d", &N);

    int (*arr)[2] = malloc(sizeof(int[2])*N);

    for (int i = 0; i<N; i++) {
        scanf("%d", &arr[i][0]);
        scanf("%d", &arr[i][1]);
    }

    qsort(arr, N, 8, cmp);

    for (int i = 0; i<N; i++) {
        printf("%d ", arr[i][0]);
        printf("%d\n", arr[i][1]);
    }

    free(arr);

    return 0;
}