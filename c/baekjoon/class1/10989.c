#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    
    int n;
    long long arr[10001] = {0};

    // 1. 파일 불러오기
    freopen("10989.txt", "r", stdin);

    // 2. 수의 개수 N, 초기화
    scanf("%d", &n);
    
    // 3. 배열에 데이터 입력 및 정렬 처리
    for (int i = 0; i < n; i++) {
        long long num;
        scanf(" %lld", &num);
        if (arr[num] != 0) {
            arr[num] += num;
        } else {
            arr[num] = num;
        }
    }

    // 4. 정렬된 데이터 출력
    for (int i = 1; i <= 10000; i++) {
        if (arr[i] != 0) {
            for (int j = 0; j<arr[i]/i; j++) {
                printf("%d\n", i);
            }
        }
    }

    return 0; 
}
