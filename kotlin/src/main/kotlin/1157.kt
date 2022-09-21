import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayList

/*
1차 시도
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
}*/

//2차 시도
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val result = ArrayList<Int>()
    val alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val word = br.readLine().uppercase()

    for (char in alpha) {
        val upperCnt = word.count {
            it == char
        }
        result.add(upperCnt)
    }

    val charMax = Collections.max(result)
    val uniqueYn = result.count {
        it == charMax
    }

    if (uniqueYn > 1) {
        print("?")
    } else {
        print(alpha[result.indexOf(charMax)])
    }
}