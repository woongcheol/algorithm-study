#include <stdio.h>
#include <string.h>

int main(void) {

    int N;

    freopen("11723.txt", "r", stdin);
    scanf("%d", &N);
    
    int nums[21] = { 0 };

    for (int i = 0; i<N; i++) {
        char cmd[7] = {0};
        int num = 0;
        scanf("%s", cmd);
        
        if (strcmp(cmd, "add") == 0)
        {
            scanf("%d", &num);
            if (nums[num] == 0)
                nums[num] = 1;   
            else
                continue;
        }
        else if (strcmp(cmd, "remove") == 0)
        {
            scanf(" %d", &num);
            if (nums[num] == 1)
                nums[num] = 0;
            else
                continue;
        }
        else if (strcmp(cmd, "check") == 0)
        {
            scanf("%d", &num);
            printf("%d\n", nums[num]);
        }
        else if (strcmp(cmd, "toggle") == 0)
        {
            scanf(" %d", &num);
            if (nums[num] == 0)
                nums[num] = 1;
            else
                nums[num] = 0;
        }
        else if (strcmp(cmd, "all") == 0)
        {
            for (int j = 1; j <= 20; j++)
            {
                nums[j] = 1;
            }
        }
        else if (strcmp(cmd, "empty") == 0)
        {
            for (int j = 1; j <= 20; j++)
            {
                nums[j] = 0;
            }
        }
    }

    return 0;
}