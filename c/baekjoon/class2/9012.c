#include <stdio.h>

#define MAX_LENGTH 52
#define YES 1
#define NO 0


int main(void) {

    freopen("9012.txt", "r", stdin);
    
    int N;

    scanf("%d\n", &N);

    for (int i = 0; i<N; i++) {

        char input[MAX_LENGTH];
        char stack[MAX_LENGTH];
        int STACK_CNT = 0;

        int result = YES;

        fgets(input, MAX_LENGTH, stdin);
        
        for (int j = 0; input[j] != '\0'; j++) {
            char word = input[j];

            if (word == '(') {
                stack[STACK_CNT++] = word;
            } else if (word == ')') {
                if (STACK_CNT == 0 ||
                    stack[--STACK_CNT] != '('
                ) {
                    result = NO;
                    break;
                }
            }
        }

        if (result == YES && STACK_CNT == 0) {
            printf("YES\n");
        } else {
            printf("NO\n");           
        }
    }

    return 0;
}