#include <stdio.h>

int main(void) {

    int n;
    
    freopen("1874.txt", "r", stdin);
    scanf("%d", &n);

    int numArr[n];
    int stack[n];

    for (int i = 0; i<n; i++) {
        int num;
        scanf("%d", &num);

        numArr[i] = num;
        stack[i] = 0;
    }

    int cnt = 0;
    int current = 0;
    int stackNum = 1;
    int resCnt = 0;
    char result[200000];
    
    while (resCnt < 2*n) {
        if (cnt != 0 && numArr[current] == stack[cnt-1]) {
            result[resCnt++] = '-';
            cnt--;
            current++;
        } else {
            stack[cnt] = stackNum;
            cnt++;
            stackNum++;
            result[resCnt++] = '+';
        }
    }

    if (cnt == 0) {
        for(int i = 0; i<resCnt; i++) {
            printf("%c\n", result[i]);
        }
    } else {
        printf("NO");
    }

    return 0;
}