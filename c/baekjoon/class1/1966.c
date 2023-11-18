#include <stdio.h>

int main(void) {

    int test_cases;

    freopen("1966.txt", "r", stdin);

    scanf("%d", &test_cases);

    for (int i = 0; i<test_cases; i++) {
        int doc_count, target_doc;

        scanf("%d%d", &doc_count, &target_doc);

        int priorities[doc_count];

        for (int j = 0; j<doc_count; j++) {
            int priority_score;

            scanf("%d", &priority_score);
            priorities[j] = priority_score;
        }

        int printed_count = 1;
        int remaining_docs = doc_count;
        int current_position = target_doc+1;

        // 우선순위 탐색
        while(remaining_docs != 0) {
            int to_print = 0;
            int current = priorities[0];

            if (remaining_docs == 1) {
                to_print = 1;
            } else {
                for (int j=1; j<remaining_docs; j++) {
                    if (current >= priorities[j]) {
                        to_print = 1;
                    } else {
                        to_print = 0;
                        break;
                    }
                }
            }

            // 출력 및 제거, 카운트 처리
            if (to_print == 1) {

                // 해당 문서가 현재 차례일 경우 출력
                if (current_position == 1) {
                    printf("%d\n", printed_count);
                    break;
                } else {
                    current_position -= 1;
                }
                
                // 해당 문서 출력시 카운트 출력
                printed_count += 1;
                to_print = 0;

                // 문서 이동
                remaining_docs -= 1;
                
                for(int j = 0; j<remaining_docs; j++) {
                    priorities[j] = priorities[j+1];
                }
            } else { // 미출력 및 뒤로 이동

                // 해당 문서가 현재 차례일 경우 뒤로 이동
                if (current_position == 1) {
                    current_position = remaining_docs;
                } else {
                    current_position -= 1;
                }

                int temp = priorities[0];

                for(int j = 0; j<remaining_docs-1; j++) {
                    priorities[j] = priorities[j+1];
                }

                priorities[remaining_docs-1] = temp;
            }
        }

        

        
    }

    return 0;
}