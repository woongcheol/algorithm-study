import java.io.BufferedReader
import java.io.InputStreamReader

// 1차
/*fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine()!!.split(' ').map {
        it.toInt()
    }

    println(a - b)
}*/

// 2차
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine().split(' ').map{
        it.toInt()
    }
    print(a - b)
}