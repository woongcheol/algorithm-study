#include <stdio.h>

int main()
{
    int a, b;  
    freopen("1000.txt", "r", stdin);
    scanf("%d %d", &a, &b);  
    printf("%d", a+b);  

    return 0;
}