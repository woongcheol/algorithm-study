import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val a = br.readLine()!!.toInt()
    val b = br.readLine()!!.toInt()
    val c = br.readLine()!!.toInt()

    val res = a * b * c
    val numList = mutableMapOf<Int, Int>()

    res.toString().forEach {
        var it = it - '0'
        if (numList.containsKey(it)) {
            numList[it] = numList[it]!!.plus(1)
        } else {
            numList.set(it, 1)
        }
    }
    for (i in 0..9) {
        if (numList[i] != null) {
            println(numList[i])
        } else {
            println(0)
        }

    }
}