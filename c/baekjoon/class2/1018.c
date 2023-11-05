#include <stdio.h>

int main(void) {

    freopen("1018.txt", "r", stdin);

    int N, M;

    scanf("%d%d", &N, &M);

    // 보드 선언 및 초기화
    char board[N][M+1];
    
    for (int i = 0; i < N; i++) {
        scanf("%s", board[i]);
    }

    // 최소값
    int min = 2500;
    char color[2] = {'W', 'B'};
    char current = 'W';
    int result[2] = {0};

    // 시작점 : 세로 A, 가로 B
    int posA = 0;
    int posB = 0;

    while (1) {

        // 보드판 순회 : 화이트 및 블랙
        for (int i = 0; i < 2; i++) {
            // printf("%d ", i);
            current = color[i];

            // 세로 순
            for (int j = posA; j <= posA + 7; j++) {
                
                // 색상 변경
                if (current == color[0]) {
                    current = color[1];
                } else {
                    current = color[0];
                }

                // 가로 순
                for (int k = posB; k <= posB + 7; k++) {
                    if (board[j][k] != current) {
                        result[i] += 1;
                    }

                    // 색상 변경
                    if (current == color[0]) {
                        current = color[1];
                    } else {
                        current = color[0];
                    }
                    
                }
            }

            // 결과 초기화
            if (result[i] < min) {
                min = result[i];
                
            }

            result[i] = 0;
        }

        // 좌표 수정
        if (N - posA <= 8 && M - posB <= 8) {
            break;
        } 
        
        if (M - posB <= 8) {
            posA += 1;
            posB = 0;
        } else {
            posB += 1;
        }

    }

    printf("%d", min);

    return 0;
}