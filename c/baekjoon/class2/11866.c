#include <stdio.h>

int main(void) {

    freopen("11866.txt", "r", stdin);

    int N, K;

    scanf("%d%d", &N, &K);

    int arr[N+1];

    for (int i = 0; i<=N; i++) {
        arr[i]=i;
    }

    int cnt = 0;
    int current = 0;
    int temp = 1;
    int result[N];
    int remove = 0;

    while (cnt<N) {

        for (int i = temp; i<=K; i++) {

            // 데이터가 1개 남았을 경우
            if (N-cnt == 1) {
                result[N-1] = arr[1];
                break;
            }

            // current 초기화
            if (N-cnt<current+i) {
                current = 1 - i;
                temp = i;
                cnt--;
                break;
            }

            // 3번째 값 삭제 및 업데이트
            if (i == K) {
                // 결과 업데이트
                result[cnt] = arr[current+i];          
                
                // 삭제 처리
                for (int j = current+i; j<=N-cnt; j++) {
                    arr[j] = arr[j+1];
                }

                current = current+i-1;
                temp=1;
            }
        }

        cnt++;
    }

    printf("<");
    for (int i = 0; i<N ; i++) {
        if (i < N-1) {
            printf("%d, ", result[i]);    
        } else {
            printf("%d", result[i]);
        }
    }
    printf(">");


    return 0;
}