import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val numList = mutableListOf<Int>()
    for (i in 0..8) {
        numList.add(br.readLine()!!.toInt())
    }
    var maxNum = 0
    for (num in numList) {
        maxNum = max(maxNum, num)
    }
    println(maxNum)
    print(numList.indexOf(maxNum)+1)
}