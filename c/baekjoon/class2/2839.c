#include <stdio.h>

int main(void) {

    freopen("2839.txt", "r", stdin);
    
    int N;

    scanf("%d", &N);

    int bags = 0;

    while (N % 5 != 0 && N > 0) {
        N -= 3;
        bags++;
    }

    if (N < 0) {
        printf("-1");
    } else {
        bags += N / 5;
        printf("%d", bags);
    }

    return 0;
}