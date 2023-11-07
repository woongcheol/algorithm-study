#include <stdio.h>

int findCardNum(int N) {
    int queue[N];
    int front = 0, rear = N-1;

    for (int i = 0; i < N; i++) {
        queue[i] = i+1;
    }

    while (front != rear) {
        front = (front + 1) % N;
        rear = (rear + 1) % N;
        queue[rear] = queue[front];
        front = (front + 1) % N;
    }

    return queue[front];
}

int main(void) {
    int N;

    freopen("2164.txt", "r", stdin);
    scanf("%d", &N);

    int result = findCardNum(N);

    printf("%d", result);

    return 0;
}
