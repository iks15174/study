import java.util.*

val b = System.`in`.bufferedReader()

fun main() {
    val (n, m) = b.readLine().split(' ').map{it.toInt()}
    val nums = b.readLine().split(' ').map{it.toInt()}.toIntArray()
    val accSum = IntArray(n)
    for(i in 0 until n) {
        val prevVal = if(i == 0) 0 else accSum[i - 1]
        accSum[i] = nums[i] + prevVal
    }
    val ans = ArrayList<Int>()
    repeat(m) {
        val (start, end) = b.readLine().split(' ').map{it.toInt()}.map{it - 1}
        val prev = if(start - 1 >= 0) accSum[start - 1] else 0
        val entire = accSum[end]
        ans.add(entire - prev)
    }
    for(a in ans) {
        println(a)
    }
}