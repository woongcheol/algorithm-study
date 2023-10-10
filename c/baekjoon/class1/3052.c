// 데이터 입력, 표준 입출력 함수 헤더 파일
#include <stdio.h>

int main(void) {
    
    // 데이터 입력
    // 1. 변수 선언
    int arr[10];

    // 2. 파일 불러오기
    freopen("3052.txt", "r", stdin);

    // 3. 정수 처리
    for (int i = 0; i<10; i++){
        int value;

        scanf("%d", &arr[i]);
    }

    // 알고리즘, 서로 다른 나머지 값 확인
    // 1. 변수 선언 및 초기화
    int mod[42] = {0};
    int result = 0;

    // 2. 나머지 값 배열에 할당
    for (int i = 0; i<10; i++) {
        mod[arr[i]%42] = 1;
    }

    // 3. 서로 다른 나머지 값 확인
    for (int i = 0; i<42; i++) {
        if (mod[i] == 1) {
            result += 1;
        }
    }

    // 4. 결과 출력
    printf("%d", result);

    return 0;
}