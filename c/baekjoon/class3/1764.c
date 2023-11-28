#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int cmp(const void* first, const void* second) {
    char *a = (char*)first;
    char *b = (char*)second;

    if (strcmp(a, b) > 0) {
        return 1;
    } else {
        return -1;
    }
}

int main(void) {

    int N, M;

    freopen("1764.txt", "r", stdin);
    scanf("%d %d", &N, &M);

    char not_heard_list[N][21];
    char not_seen_list[M][21];
    // char sorted_list = NULL;


    // sorted_list = (char*)malloc(N * sizeof(char));

    for (int i = 0; i<N; i++) {
        char name[21];
        scanf("%s", name);

        for (int j = 0; name[j] != '\0'; j++) {
            not_heard_list[i][j] = name[j];

            if (name[j+1] == '\0') {
                not_heard_list[i][j+1] = '\0';
            }
        }

    }

    for (int i = 0; i<M; i++) {
        char name[21];
        scanf("%s", name);

        for (int j = 0; name[j] != '\0'; j++) {
            not_seen_list[i][j] = name[j];

            if (name[j+1] == '\0') {
                not_seen_list[i][j+1] = '\0';
            }
        }
    }

    qsort(not_heard_list, N, sizeof(char[21]), cmp);
    qsort(not_seen_list, M, sizeof(char[21]), cmp);

    int condition;

    if (N>M) {
        condition = M;
    } else {
        condition = N;
    }

    char temp[condition][21];
    int cnt = 0;

    for (int i = 0; i < condition; i++) {
        int left = 0, right, mid;
        if (N > M) {
            right = N;
        } else {
            right = M;
        }
    
        while (left <= right)
        {
            mid = (left + right) / 2;

            if (N > M) {
                if (strcmp(not_heard_list[mid], not_seen_list[i]) == 0) {
                    for (int j = 0; not_seen_list[i][j] != '\0'; j++) {
                        temp[cnt][j] = not_seen_list[i][j];

                        if (not_seen_list[i][j+1] == '\0') {
                            temp[cnt][j+1] = '\0'; 
                        }
                    }

                    cnt += 1;
                    break;
                } else if (strcmp(not_heard_list[mid], not_seen_list[i]) > 0) {
                    right = mid - 1 ;
                } else {
                    left = mid + 1;
                }
            } else {
                if (strcmp(not_seen_list[mid], not_heard_list[i]) == 0) {
                    for (int j = 0; not_heard_list[i][j] != '\0'; j++) {
                        temp[cnt][j] = not_heard_list[i][j];

                        if (not_heard_list[i][j+1] == '\0') {
                            temp[cnt][j+1] = '\0'; 
                        }
                    }

                    cnt += 1;
                    break;
                } else if (strcmp(not_seen_list[mid], not_heard_list[i]) > 0) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
    }

    printf("%d\n", cnt);

    for (int i = 0; i<cnt; i++) {
        printf("%s\n", temp[i]);
    }

    return 0;
}