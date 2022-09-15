import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val T = br.readLine()!!.toInt()
    for (i in 1..T) {
        var res = ""
        var (R, S) = br.readLine()!!.split(' ')
        for (i in S) {
            res += i.toString().repeat(R.toInt())
        }
        println(res)
    }
}