#include <stdio.h>

int main(void) {

    freopen("10773.txt", "r", stdin);
    
    int K;
    int arr[100000] = {0};
    int cnt = 0;

    scanf("%d\n", &K);

    for (int i = 0; i<K; i++) {
        int num;

        scanf("%d", &num);
        if (num != 0) {
            arr[cnt++] = num;
        } else {
            arr[--cnt] = 0;
        }
    }

    int sum = 0;

    for (int i = 0; i<cnt; i++) {
        sum += arr[i];
    }

    printf("%d", sum);

    return 0;
}