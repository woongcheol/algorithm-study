#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int num;
    char name[21];
} names;

int cmp(const void* first, const void* second) {
    names *a = (names*)first;
    names *b = (names*)second;

    if (strcmp(a->name, b->name) > 0) {
        return 1;
    } else {
        return -1;
    }
}

int main(void) {

    int N, M;

    freopen("1620.txt", "r", stdin);
    scanf("%d %d", &N, &M);

    names* list = NULL;
    names* sorted_list = NULL;

    list = (names*)malloc(N * sizeof(names));
    sorted_list = (names*)malloc(N * sizeof(names));

    for (int i = 0; i<N; i++) {
        char name[21];
        scanf("%s", name);

        list[i].num = sorted_list[i].num = i+1;

        for (int j = 0; name[j] != '\0'; j++) {
            list[i].name[j] = sorted_list[i].name[j] = name[j];

            if (name[j+1] == '\0') {
                list[i].name[j+1] = sorted_list[i].name[j+1] ='\0';
            }
        }
    }

    qsort(sorted_list, N, sizeof(sorted_list[0]), cmp);

    for (int i = 0; i<M; i++) {
        char name[21];
        int num;
        scanf("%s", name);

        num = atoi(name);

        if (num != 0) {
            printf("%s\n", list[num-1].name);     
        } else {
            int left, right, mid;
            left = 0;
            right = N-1;

            while (left <= right)
            {
                mid = (left + right) / 2;

                if (strcmp(sorted_list[mid].name, name) == 0) {
                    printf("%d\n", sorted_list[mid].num);
                    break;
                } else if (strcmp(sorted_list[mid].name, name) > 0) {
                    right = mid - 1 ;
                } else {
                    left = mid + 1;
                }
            }
            
        }
    }

    free(sorted_list);
    free(list);

    return 0;
}