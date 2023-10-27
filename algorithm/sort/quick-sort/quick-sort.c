#include <stdio.h>
#include <stdlib.h>

int* quicksort(int q[], int qLength) {

    if (qLength <= 1) {
        return q;
    }

    int pivot = q[0];
    int *less = (int*)malloc(sizeof(int) * qLength);
    int lessSize = 0;

    int *greater = (int*)malloc(sizeof(int) * qLength);
    int greaterSize = 0;
    
    for (int i = 1; i<qLength; i++) {
        if(pivot <= q[i]) {
            greater[greaterSize++] = q[i];
        } else {
            less[lessSize++] = q[i];
        }
    }

    int *result = (int*)malloc(sizeof(int) * qLength);

    int *sortedLess = quicksort(less, lessSize);
    int *sortedGreater = quicksort(greater, greaterSize);

    for (int i = 0; i < lessSize; i++) {
        result[i] = sortedLess[i];
    }

    result[lessSize] = pivot;

    for (int i = 0; i < greaterSize; i++) {
        result[lessSize + 1 + i] = sortedGreater[i];
    }

    free(less);
    free(greater);


    return result;
        
}

int main(void) {

    int a[] = {1, 3, 4, 7, 0, 1, 3, 4};
    int n = sizeof(a) / sizeof(a[0]);

    int *result = quicksort(a, n);

    for (int i = 0; i < n; i++) {
        printf("%d ", result[i]);
    }

    free(result);
    
    return 0;
}