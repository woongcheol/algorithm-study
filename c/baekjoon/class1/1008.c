#include <stdio.h>

// 1112kb, 0ms
int main(void) {
    double a, b;
    freopen("1008.txt", "r", stdin);
    scanf("%lf %lf", &a, &b);
    printf("%.9lf", a/b);
}