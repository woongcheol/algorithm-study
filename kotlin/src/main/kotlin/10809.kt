import java.io.*

fun main () {
    // 데이터 입력
    val br = BufferedReader(InputStreamReader(System.`in`));
    val inputData = br.readLine()

    // 변수 선언 및 할당
    val alphaMap = IntArray(26){-1}

    // 데이터 출력
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    // 순회
    for (letter in inputData.indices) {
        if (alphaMap[inputData[letter].toInt()-97] == -1) {
            alphaMap[inputData[letter].toInt() - 97] = letter
        }
    }

    alphaMap.forEach { bw.write("${it} ") }

    // 출력 비우기 및 종료
    bw.flush()
    bw.close()
}