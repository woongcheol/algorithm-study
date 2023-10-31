/*
복기
- javascript와 차이
- cmp 함수
- qsort 함수
- 문자열 \n 처리

*/

#include <stdio.h>
#include <string.h>

int compare(const void* arg1, const void* arg2) 
{   
    return strcmp((char*)arg1, (char*)arg2);
} 

void createLowerCaseWordArray(char arr[][50], int numList[], int N) {
    for (int i = 0; i <= N; i++) {
        char word[50] = {0};
        int cnt = 0;

        // 단어 길이 저장
        for (int j = 0; j < 50; j++) {
            char temp;

            // 입력 실패 시 루프 종료
            if (scanf("%c", &temp) != 1) {
                break;
            }

            // 줄 바꿈 문자를 입력받으면 루프 종료
            if (temp == '\n') {
                break;
            }

            word[j] = temp;
            cnt++;
        }

        numList[i] = cnt;

        // 배열에 단어 입력
        strcpy(arr[i], word);
    }
}

int main(void) {

    // 1. 파일 불러오기
    freopen("1181.txt", "r", stdin);

    // 2. 단어 개수 입력
    int N;
    scanf("%d", &N);

    // 3. 소문자 단어 배열 생성
    char arr[N+1][50];
    int numList[N+1];

    createLowerCaseWordArray(arr, numList, N);

    // 4. 정렬
    int sortedList[N];

        for (int i = 1; i <= 50; i++) {
        char tempWord[N][50];
        char resultWord[N][50];
        int rcnt = 0;
        int cnt = 0;
        int isTemp = 0;
        
            // 길이 순 정렬
            for (int j = 1; j <= N; j++) {
                if (numList[j] == i) {
                    strcpy(tempWord[cnt], arr[j]);
                    isTemp = 1;
                    cnt++;
                }
            }

            // 사전 순 정렬
            if(isTemp && 1<=cnt) {
                qsort(tempWord, cnt, 50, compare);
            }

            if(isTemp) {
                // 중복 단어일 경우 제외 처리
                for (int k = 0; k< cnt; k++) {
                    
                    if (1<=k && !strcmp(tempWord[k], tempWord[k-1])) {
                        continue;
                    }

                    strcpy(resultWord[rcnt], tempWord[k]);
                    rcnt++;
                }

                for (int k = 0; k < rcnt; k++) {
                    printf("%s\n", resultWord[k]);
                }
            }
    }

    return 0;
}