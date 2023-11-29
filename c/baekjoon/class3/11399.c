#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    int numA = *(int *)a;
    int numB = *(int *)b;

    if(numA==numB) {
        return numA == numB;
    } else {
        return (numA > numB);
    }
}

int main(void) {

    int N;

    freopen("11399.txt", "r", stdin);
    scanf("%d", &N);

    int arr[N];

    for (int i = 0; i<N; i++) {
        int num;
        scanf("%d", &num);
        arr[i] = num;
    }

    qsort(arr, N, sizeof(int), cmp);

    int result = 0;

    for (int i = 0; i<N; i++) {
        result += arr[i];
        for (int j = i; j+1<N; j++) {
            result += arr[i];
        }
    }

    printf("%d", result);

    return 0;

}