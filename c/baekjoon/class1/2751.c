#include <stdio.h>
#include <stdlib.h>

int main(void) {

    freopen("2751.txt", "r", stdin);
    
    int N;

    scanf("%d", &N);
    
    int arr[2000002];

    for (int i = 0; i < 2000002; i++) {
        arr[i] = -1000001;
    }

    
    for (int i = 0; i<N; i++){
        int num;
        scanf("%d", &num);

        // -1,000,000 ~ 0 (1000001)
        if(num<=0) {
            arr[1000000-abs(num)] = num; // 1000000~0
        
        // 1 ~ 1,000,000
        } else if (0<num) { 
            arr[1000000+num] = num;
        }
    }

    for (int j = 0; j<=2000001; j++) {
        if(arr[j] == -1000001) {
        } else {
            printf("%d\n", arr[j]);
        }
    }

    return 0;
}