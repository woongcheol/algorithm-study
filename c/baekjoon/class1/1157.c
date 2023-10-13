// ( 데이터 입력부 )

// 1. 라이브러리 불러오기
#include <stdio.h> // 표준 라이브러리

// < Entry >
int main(void) {

    // 2. 파일 불러오기
    freopen("1157.txt","r",stdin);

    // ( 알고리즘 입력부 )
    // 1. 데이터 변환
    char arr[1000000];

    scanf("%s", arr);

    // 2. 적용
    int cnt[26]={0};

    int i = 0;
    
    while (arr[i]) {
        if (arr[i] >= 'a') {
            ++cnt[arr[i]-'a'];
        }
        else ++cnt[arr[i] - 'A'];
        ++i;
    }

    int max = 0, same = 0, index;
    char result;

    for (int i = 0; i<26; i++) {
        if (cnt[i] > max) {
            max = cnt[i];
            index = i;
            same = 0;
        } else if (cnt[i] == max) {
            same = 1;
        }
    }

    // ( 데이터 출력부 )
    if ( same == 1) printf("%c", '?');
    else printf("%c", index+65);
    
    // < Exit >
    return 0;

}