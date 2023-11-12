#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 20000000

int main(void) {

    freopen("10816.txt", "r", stdin);
    
    int N;

    scanf("%d\n", &N);

    // 카드 배열 선언
    int cards[MAX_LENGTH+1] ={0};

    for (int i = 0; i<N; i++) {
        int num;
        scanf("%d", &num);

        if (num<=0) {
            cards[MAX_LENGTH/2-abs(num)] += 1;
        } else {
            cards[MAX_LENGTH/2+num] += 1;
        }
    }

    // 카드 탐색

    int M;

    scanf("%d", &M);

    for (int i = 0; i<M; i++) {
        int num;
        scanf("%d", &num);

        if (num <= 0) {
            printf("%d ", cards[MAX_LENGTH/2 - abs(num)]);
        } else {
            printf("%d ", cards[MAX_LENGTH/2 + num]);
        }
    }

    return 0;
}