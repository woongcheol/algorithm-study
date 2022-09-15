import java.io.*
import java.lang.Integer.max
import java.util.StringTokenizer

fun main() {

    val br = BufferedReader(InputStreamReader(System.`in`))

    val n = br.readLine().toInt()
    val scoreAll = StringTokenizer(br.readLine())
    var arr = IntArray(n)
    var m = 0
    var sum = 0.00

    for (i in 1..n) {
        var score = scoreAll.nextToken().toInt()
        m = max(m, score)
        arr[i - 1] = score
    }

    for (i in arr) {
        sum += 100.00 * i / m
    }

    println(sum / n)
    br.close()

}