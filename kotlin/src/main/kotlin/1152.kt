import java.io.*
import java.util.*

/*
1차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val rs = StringTokenizer(br.readLine())

    println(rs.countTokens())
    br.close()
}*/

/*
2차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var cnt = 0
    val word = br.readLine().split(" ").map {
        if (it.length == 0) {
        } else {
            cnt += 1
        }
    }
    print(cnt)
}*/

// 3차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val tokenizer = StringTokenizer(br.readLine())
    print(tokenizer.countTokens())
    br.close()
}