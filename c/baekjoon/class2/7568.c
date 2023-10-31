#include <stdio.h>

int main(void) {

    freopen("7568.txt", "r", stdin);
    
    int N;

    scanf("%d", &N);

    int person[N+1][2];

    for (int i=0; i<N; i++) {
        int weight, height;
        scanf("%d%d",&weight, &height);
        person[i][0] = weight;
        person[i][1] = height;
    }

    for (int i = 0; i<N; i++) {
        int cnt = 1;

        for (int j = 0; j<N; j++) {
            if(person[i][0] < person[j][0] && person[i][1] < person[j][1]) {
                cnt++;
            }
        }

        printf("%d ", cnt);
    }

    return 0;

}