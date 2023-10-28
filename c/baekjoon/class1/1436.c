#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main(void){

    // 파일 불러오기
    freopen("1436.txt", "r", stdin);
    
    // 변수 선언, N번째 영화
    int N;

    // 데이터 불러오기
    scanf("%d", &N);

    // 알고리즘
    int cnt = 0;
    int result = 666;
    
    while(true) {
        char str_result[9];
        sprintf(str_result, "%d", result);

        if (strstr(str_result, "666") != NULL) {
            cnt++;
        }

        if (cnt == N) {
            break;
        }

        result++;
    }

    printf("%d", result);
    
    return 0;
}