#include <stdio.h>

/*
복기
1. 제한 사항
    - 시간 제한 : 1초
    - 메모리 제한 : 256MB
    - 데이터 : 1 ≤ N ≤ 10, 0 ≤ K ≤ N 

2. Division by zero
    - 원인) N, K가 0일 경우 나눗셈 연산에서 문제 발생
      int factN = N, factK = K, factNK = N - K;
      int result = factN/(factK*factNK);
*/

int main(void) {

    int N=0, K=0;
    
    // 1. 파일 불러오기
    freopen("11050.txt", "r", stdin);

    // 2. 데이터 입력
    scanf("%d%d", &N, &K);

    // 3. 이항 계수
    int factN = 1, factK = 1, factNK = 1;

    for (int i = 2; i <= N; i++) {
        factN *= i;
    }

    for (int j = 2; j <= K; j++) {
        factK *= j;
    }

    for (int k = 2; k <= N - K; k++) {
        factNK *= k;
    }

    int result = factN/(factK*factNK);

    // 3. 데이터 출력
    printf("%d", result);

    return 0;
}