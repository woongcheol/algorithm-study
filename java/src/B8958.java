import java.io.*;

public class B8958 {
    public static void main(String[] args) throws IOException {
        // 데이터 입력
        // 1. 변수 선언 및 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 2. 데이터 입력, TC
        int tc = Integer.parseInt(br.readLine());

        // 알고리즘
        // 1. TC 검증
        for (int i = 0; i < tc; i++) {
            // 2. 변수 선언 및 초기화
            int result = 0;
            int consecutiveSum = 0;
            boolean isConsecutive = false;
            char[] quizResult = br.readLine().toCharArray();

            for (char s : quizResult) {
                if (isConsecutive && s == 'O') {
                    consecutiveSum += 1;
                    result += consecutiveSum;
                } else if (s == 'O') {
                    result += 1;
                    consecutiveSum += 1;
                    isConsecutive = true;
                } else {
                    consecutiveSum = 0;
                    isConsecutive = false;
                }
            }

            // 3. 결과 출력
            bw.write(String.valueOf(result));
            bw.newLine();
        }

        // 마무리
        br.close();
        bw.flush();
        bw.close();

    }
}
