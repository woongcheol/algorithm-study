#include <stdio.h>

int main(void) {

    freopen("10814.txt", "r", stdin);
    
    int N;

    scanf("%d", &N);

    int age[N+1];
    char name[N+1][101];

    for (int i=0; i<N;i++) {
        scanf("%d", &age[i]);
        scanf("%s", name[i]);
    }

    int num = 1;

    while(num<201) {
        for (int i=0; i<N; i++) {
            if (age[i] == num) {
                printf("%d %s\n", age[i], name[i]);
            }
        }

        num++;
    }


    return 0;
}