#include <stdio.h>

#define MAX_LENGTH 1000001

int main(void) {

    int M, N, arr[MAX_LENGTH] = {0};
    int cnt = 0;
    arr[1] = 1;

    freopen("1929.txt", "r", stdin);

    scanf("%d %d", &M, &N);

    for (int i = 2; i<=N; i++) {
        for (int j = 2; j*i<=N; j++) {
            cnt += 1;
            if (i%j == 0 && i != j) {
                break;
            } else {
                arr[i*j] = 1;
            }
        }
    }

    for (int i = M; i<=N; i++) {
        if (arr[i] == 0) {
            // printf("%d\n", i);
        }
    }

    printf("%d\n", cnt);

    return 0;
}