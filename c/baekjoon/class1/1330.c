#include <stdio.h>

// 1116kb, 0ms
int main(void) {
    int a, b;
    freopen("1330.txt", "r", stdin);
    scanf("%d %d", &a, &b);

    if (a > b) {
        printf(">");
    } else if (a < b)
    {
        printf("<");
    } else {
        printf("==");
    }

    return 0;
}