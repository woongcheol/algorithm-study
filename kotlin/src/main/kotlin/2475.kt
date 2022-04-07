import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val num = br.readLine()!!.split(' ').map {
        it.toDouble().pow(2)
    }
    var sum = 0.0
    var result = 0.0
    for (i in num) {
        sum += i
    }

    result = sum % 10
    print(result.toInt())
}