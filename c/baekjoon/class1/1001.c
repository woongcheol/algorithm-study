#include <stdio.h>

int main(void) {
    int a, b;
    freopen("1001.txt", "r", stdin);
    scanf("%d %d", &a, &b);
    printf("%d", a-b);

    return 0;
}