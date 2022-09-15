import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val str = readLine()!!
    val map = mutableMapOf<Char, Int>()

    str.forEach {
        var char = it.toLowerCase()

        if (map.containsKey(char)) {
            map[char] = map[char]!!.plus(1)
        } else {
            map.set(char, 1)
        }
    }

    val max = map.maxOf {
        it.value
    }

    if (map.filter { it.value == max!! }.count() > 1) {
        println("?")
    } else {
        val word = map.filterValues { it == max }.keys.toString()
        println(word[1].toUpperCase())
    }
}