#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int compare(const void* a, const void* b) {
    int numA = *((int *)a);
    int numB = *((int *)b);

    return (numA > numB) - (numA < numB);
}

int main(void) {
    int N;
    
    freopen("18110.txt", "r", stdin);

    scanf("%d", &N);

    if (N == 0) {
        printf("0");
    } else {
        int sum[N];
        int removePerson = round(N * 0.3 / 2);

        for (int i = 0; i<N; i++) {
            int num;
            scanf("%d", &num);

            sum[i] = num;
        }

        qsort(sum, N, sizeof(int), compare);

        for (int i = 0; i<removePerson; i++) {
            sum[i] = 0;
            sum[N-i-1] = 0;
        }
        
        double result = 0; 

        for (int i = 0; i<N; i++) {
            result += sum[i];
        }

        printf("%.0f", round(result / (N - removePerson * 2)));

    }

    return 0;
}