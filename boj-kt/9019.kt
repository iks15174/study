import java.util.*

val br = System.`in`.bufferedReader()

fun Dchange(n: Int): Int {
    return (n * 2) % 10000
}

fun Schange(n: Int): Int {
    return if (n == 0) 9999 else n - 1
}

fun Lchange(n: Int): Int {
    return (n % 1000) * 10 + n / 1000
}

fun Rchange(n: Int): Int {
    return (n % 10) * 1000 + (n / 10)
}


fun main() {
    val t = br.readLine().toInt()
    repeat(t) {
        val (curVal, targetVal) = br.readLine().split(' ').map{it.toInt()}
        val visitedNum = BooleanArray(10000){false}
        val queue = LinkedList<Pair<Int, String>>(listOf(Pair(curVal, "")))
        val move = listOf("D", "S", "L", "R")
        while(queue.size > 0) {
            val curPair = queue.poll()
            if(curPair.first == targetVal){
                println(curPair.second)
                break
            }
            for(m in move) {
                if(m == "D") {
                    val newVal = Dchange(curPair.first)
                    if(visitedNum[newVal].not()){
                        visitedNum[newVal] = true
                        queue.add(Pair(newVal, curPair.second + "D"))
                    }
                }
                if(m == "S") {
                    val newVal = Schange(curPair.first)
                    if(visitedNum[newVal].not()){
                        visitedNum[newVal] = true
                        queue.add(Pair(newVal, curPair.second + "S"))
                    }
                }  
                if(m == "L") {
                    val newVal = Lchange(curPair.first)
                    if(visitedNum[newVal].not()){
                        visitedNum[newVal] = true
                        queue.add(Pair(newVal, curPair.second + "L"))
                    }
                }  
                if(m == "R") {
                    val newVal = Rchange(curPair.first)
                    if(visitedNum[newVal].not()){
                        visitedNum[newVal] = true
                        queue.add(Pair(newVal, curPair.second + "R"))
                    }
                }  
            }
        }
    }
}