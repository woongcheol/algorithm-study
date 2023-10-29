#include <stdio.h>

int main(void) {

    int N;
    
    freopen("1676.txt", "r", stdin);
    scanf("%d", &N);

    int a=0, b=0;

    for (int i = 2; i<=N; i++) {
        int x = i;

        while (x%2 == 0)
        {   
            x/=2;
            a++;
        }

        while (x%5 == 0) {
            x/=5;
            b++;
        }
    }
    
    if (a<b) printf("%d", a);
    else printf("%d", b);

    return 0;
}