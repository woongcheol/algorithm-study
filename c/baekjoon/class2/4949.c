#include <stdio.h>

#define MAX_LENGTH 102
#define YES 1
#define NO 0

int main(void) {
    freopen("4949.txt", "r", stdin);

    char input[MAX_LENGTH];
    char stack[MAX_LENGTH];
    int stack_top = 0;
    
    while (1) {
        fgets(input, MAX_LENGTH, stdin);

        if (input[0] == '.') {
            break;
        }

        int result = YES;

        for (int i = 0; input[i] != '\n'; i++) {
            char alpha = input[i];

            if (alpha == '(' || alpha == '[') {
                stack[stack_top++] = alpha;
            } else if (alpha == ')' || alpha == ']') {
                if (stack_top == 0 || 
                    (alpha == ')' && stack[--stack_top] != '(') ||
                    (alpha == ']' && stack[--stack_top] != '[')) {
                    result = NO;
                    break;
                }
            }
        }

        if (result == YES && stack_top == 0) {
            printf("yes\n");
        } else {
            printf("no\n");
        }

        // 스택 초기화
        stack_top = 0;
    }

    return 0;
}