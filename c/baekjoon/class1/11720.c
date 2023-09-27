#include <stdio.h>

int main(void) {
    int n, sum = 0;
    
    freopen("11720.txt", "r", stdin);
    
    scanf("%d", &n);
    char arr[n-1];

    scanf("%s", &arr);

    for (int i = 0; i < n; i++) {
        sum += arr[i] - '0';
    }
    printf("%d", sum);
}