import java.io.BufferedReader
import java.io.InputStreamReader

/* 1차 도전
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine()!!.split(' ').map {
        it.toDouble()
    }

    val res = a / b
    println(res)
}*/

// 2차 도전
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine().split(' ').map{
        it.toDouble()
    }
    print(a/b)
}