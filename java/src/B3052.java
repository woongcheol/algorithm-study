import java.io.*;
import java.util.LinkedHashMap;

public class B3052 {
    public static void main(String[] args) throws IOException {
        // 데이터 입력
        // 1. 변수 선언, 데이터 입력 및 출력을 위한 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 알고리즘, 서로 다른 나머지 값 확인
        // 1. 변수 선언 및 초기화
        LinkedHashMap<Integer, Integer> map = new LinkedHashMap<>();

        // 2. 나머지 값, Map에 할당
        for (int i = 0; i < 10; i++) {
            int rest = Integer.parseInt(br.readLine()) % 42;
            if (!map.containsKey(rest)) {
                map.put(rest, 0);
            }
        }

        // 3. 서로 다른 나머지 값 확인
        int answer = 0;
        for (Integer num : map.keySet()) {
            answer++;
        }

        // 4. 결과 출력
        bw.write(String.valueOf(answer));
        br.close();
        bw.flush(); // 버퍼 비우기
        bw.close(); // BufferedWriter 닫기
    }
}
