#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int findCm(int requiredCuts, unsigned int start, unsigned int end, unsigned int lanLengths[], int numLans) {

    if (start > end) {
        return end;
    }

    int mid = start + (end - start)/2;

    if (mid == 0) {
        mid = 1;
    }

    int cuts = 0;

    for (int i = 0; i<numLans; i++) {
        cuts += floor(lanLengths[i]/mid);
    }

    if (requiredCuts <= cuts) {
        return findCm(requiredCuts, mid+1, end, lanLengths, numLans);
    } else if (requiredCuts > cuts) {
        return findCm(requiredCuts, start, mid-1, lanLengths, numLans);
    }
}

int main(void) {

    int K, N;

    freopen("1654.txt", "r", stdin);

    scanf("%d %d", &K, &N);

    unsigned int arr[K];
    int max = 0;

    for (int i = 0; i < K; i++) {
        unsigned num;
        scanf("%d", &num);

        if (max < num) {
            max = num;
        }

        arr[i] = num;
    }

    int maxCm;

    maxCm = findCm(N, 0, max, arr, K);
    printf("%d", maxCm);

    return 0;
}