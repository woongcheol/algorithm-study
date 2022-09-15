import java.io.BufferedReader
import java.io.InputStreamReader

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