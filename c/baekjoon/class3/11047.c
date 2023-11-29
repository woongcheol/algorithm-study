#include <stdio.h>

int main(void) {

    int N, K;

    freopen("11047.txt", "r", stdin);
    scanf("%d %d", &N, &K);

    int arr[N];
    int cnt = 0;

    for (int i = 0; i<N; i++) {
        int num;

        scanf("%d", &num);
        
        if (K/num > 0) {
            cnt += 1;
            arr[i] = num;
        } else {
            break;
        }
    }

    int result = 0;

    while (K!=0) {
        int coin = arr[--cnt];

        int cointCnt = K / coin;
        result += cointCnt;

        K -= coin*cointCnt;
    }

    printf("%d", result);


    return 0;
}