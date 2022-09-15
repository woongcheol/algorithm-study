import java.io.BufferedReader
import java.io.InputStreamReader

/* 1차 - readLine + split
fun main() {
    val (a, b) = readLine()!!.split(' ')
    println(a.toInt() + b.toInt())
}*/

/*2차 - BufferedReader
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (c, d) = br.readLine()!!.split(' ').map {
        it.toInt()
    }
    println(c + d)
} */

// 3차
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine().split(' ').map {
        it.toInt()
    }
    print(a+b)
}