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

#include <stdio.h>

int main(void) {

    int N=0, K=0;
    
    // 1. 파일 불러오기
    freopen("11050.txt", "r", stdin);

    // 2. 데이터 입력
    scanf("%d%d", &N, &K);

    // 3. 이항 계수
    int result = factorial(N) / (factorial(K) * factorial(N - K));

    // 4. 데이터 출력
    printf("%d", result);

    return 0;
}

// 팩토리얼 계산 함수
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }

    int result = 1;
    
    for (int i = 2; i <= n; i++) {
        result *= i;
    }

    return result;
}