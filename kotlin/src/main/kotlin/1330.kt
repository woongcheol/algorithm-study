import java.io.BufferedReader
import java.io.InputStreamReader

/*1차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine()!!.split(' ').map {
        it.toShort()
    }

    if (a > b) {
        println(">")
    } else if (a < b) {
        println("<")
    } else {
        println("==")
    }
}
*/

// 2차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (a, b) = br.readLine().split(' ').map {
        it.toInt()
    }

    when {
        (a < b) -> print("<")
        (a > b) -> print(">")
        (a == b) -> print("==")
    }
}