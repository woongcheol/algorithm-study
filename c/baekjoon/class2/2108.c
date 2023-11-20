#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LENGTH 8001

int main(void) {

    int N;
    int arr[MAX_LENGTH] = {0};

    // 산술평균 : 누적합
    int sum = 0;

    // 범위 : 최댓값, 최솟값
    int max = -4001, min = 4001;

    freopen("2108.txt", "r", stdin);

    scanf("%d", &N);

    // 정수 입력
    for (int i = 0; i<N; i++) {
        int num;
        scanf("%d", &num);

        // 산술 평균 : 누적합 / 나누기
        sum += num;

        // 최빈값, 중앙값 : 배열 값 갱신 및 절대값
        if (num<0) {
            arr[4000-abs(num)] += 1;
        } else {
            arr[4000+num] += 1;
        }

        // 범위 : 최댓값, 최솟값
        if (min > num) {
            min = num;
        } 
        
        if (num > max) {
            max = num;
        }
    }

    // 산술 평균
    printf("%d\n", (int)round((float)sum/N));

    // 중앙값 및 최빈값
    // 중앙값 관련
    int midNum;
    int cnt;
    if (N == 1) {
        midNum = 1;
        cnt = 0;
    } else {
        midNum = N / 2;
        cnt = -1;
    }
    
    // 최빈값 관련
    int maxCnt = 0;
    int minNum = 1;
    int minSecondNum = 8001;

    for (int i = 0; i<MAX_LENGTH; i++) {

        // 입력된 값이 있을 경우
        if (arr[i] != 0) {

            // 중앙값 관련 카운트
            cnt += arr[i];

            // 최빈값 관련 카운트
            if (maxCnt < arr[i]) {
                maxCnt = arr[i];
                minNum = i;
                minSecondNum = 8001;
            } else if (maxCnt == arr[i]) {
                if (minNum < i && minSecondNum > i) {
                    minSecondNum = i;
                }
            }
        }

        // 중앙값일 시 출력
        if (cnt > 0 && cnt >= midNum) {
            printf("%d\n", i - 4000);
            midNum = 500001;
        }
    }

    // 최빈값
    if (minSecondNum != 8001) {
        printf("%d\n", minSecondNum - 4000);
    } else {
        printf("%d\n", minNum - 4000);
    }

    // 범위
    printf("%d\n", max-min);

    return 0;
}