import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine()!!.toInt()

    for (i in 1..n) {
        println(" ".repeat(n - i)+"*".repeat(i))
    }
}