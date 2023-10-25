#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
복기
1. 제한 사항
    - 시간 제한 : 5초
    - 메모리 제한 : 8MB
    - 언어 제한 : javascript

2. 시간 제한에 대하여
    - 정렬 알고리즘 관련, 최악의 경우 n = 10,000,000에서 quick sort의 O(n^2)의 1e+14번의 연산으로 시간 초과가 발생한다.
    - for 문의 counter의 자료형을 short로 바꾸면 성능이 저하된다. 이는 현대 아키텍쳐에서 레지스터(32비트) 처리되는 것과 관련이 있는데
      short는 2바이트 크기를 가지므로 레지스터(16비트)에서 데이터를 여러번 옮겨야하는 오버헤드가 발생할 수 있다고 한다.

3. 메모리 제한에 대하여
    - 정렬 알고리즘 관련, 정렬에 필요한 배열 생성 시 n = 10,000,000, data = 10,000(구조체 정의 기준, 최소 14비트)에 따라
      10,000,000 * 14비트 = 약 17MB의 메모리가 필요함을 알 수 있다.
    - C의 기본량은 약 1112KB(C++, 2024KB)

4. 이로 인해, 정렬 알고리즘을 활용했을 경우 시간과 메모리 제한으로 인해 문제를 풀지 못하므로 O(n)에서 수행할 수 있는 방법을 적용해야한다.

5. 하단 알고리즘은 최악의 경우 O(2n)의 연산을 수행하는 알고리즘으로 최대 20,000,000 연산을 수행하여 주어진 조건 하에 동작할 수 있었다.
    - 언어 : C99
    - 사용 메모리 : 1112kb
    - 수행 시간 : 2620ms

*/

int main(void) {
    
    int n;
    int arr[10001] = {0}; // 최대 10,000 * 4바이트 = 40KB

    // 1. 파일 불러오기
    freopen("10989.txt", "r", stdin);

    // 2. 수의 개수 N, 초기화
    scanf("%d", &n);
    
    // 3. 배열 선언
    // - O(n), 최대 10,000,000번의 연산 수행
    for (int i = 0; i < n; i++) {
        short num;
        scanf(" %hd", &num);
        arr[num] += 1;
    }

    // 4. 배열 순회
    // - O(n), 최대 10,000,000번의 연산 수행
    for (int i = 1; i <= 10000; i++) {
        if (arr[i] != 0) {
            for (int j = 0; j<arr[i]; j++) {
                printf("%d\n", i);
            }
        }
    }

    return 0; 
}