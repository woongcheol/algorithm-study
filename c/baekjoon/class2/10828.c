#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 10000

int main(void) {

    freopen("10828.txt", "r", stdin);
    
    int N;

    scanf("%d\n", &N);

    int nums[MAX_LENGTH] = {0};
    int cnt = 0;

    for (int i = 0; i<N; i++) {
        char arr[6] = {0};
        int num = 0;
        scanf("%s%d", arr, &num);

        if (strcmp(arr, "push") == 0) {
            nums[cnt++] = num;
        } else if (strcmp(arr, "pop") == 0) {
            if (cnt != 0) {
                printf("%d\n", nums[--cnt]);
            } else {
                printf("%d\n", -1);
            }
        } else if (strcmp(arr, "size") == 0) {
            printf("%d\n", cnt);
        } else if (strcmp(arr, "top") == 0) {
            if (cnt != 0) {
                printf("%d\n", nums[--cnt]);
                cnt++;
            } else {
                printf("%d\n", -1);
            }
        } else if (strcmp(arr, "empty") == 0) {
            if (cnt != 0) {
                printf("%d\n", 0);
            } else {
                printf("%d\n", 1);
            }
        }
    }

    return 0;
}