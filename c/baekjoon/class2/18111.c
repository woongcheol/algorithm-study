#include <stdio.h>

int main(void) {

    int N, M, B;

    freopen("18111.txt", "r", stdin);

    scanf("%d%d%d", &N, &M, &B);

    int arr[N][M];
    int max = 0;

    for (int i = 0; i<N; i++) {
        for (int j = 0; j<M; j++) {
            int num;
            scanf("%d", &num);
            arr[i][j] = num;

            if (max < num) {
                 max = num;
            }
        }
    }

    int min = 2147483647;

    while(max != -1) {
        int add = 0, remove = 0;
        int isFlat = 0;

        for (int i = 0; i<N; i++) {
            for (int j = 0; j<M; j++) {
                if(max > arr[i][j]) {
                    add += (max - arr[i][j]);
                } else if (max < arr[i][j]) {
                    remove += (arr[i][j] - max);
                }
            }
        }

        int addTime = add * 1;
        int removeTime = remove * 2;
        int totalTime = 0;

        if (B >= add) {
            isFlat = 1;
            totalTime = addTime + removeTime;
        } else if (B + remove >= add) {
            isFlat = 1;
            totalTime = addTime + removeTime;
        }

        if (isFlat && min > totalTime) {
            min = totalTime;
        } else if (isFlat && min <= totalTime) {
            break;
        }        

        max -= 1;
    }
    
    printf("%d %d", min, max+1);

    return 0;
}