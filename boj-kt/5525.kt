

fun main(){
    val n = readLine()!!.toInt()
    val stringLength = readLine()
    val ss = readLine()
    var validStrLen = 0
    var expectedVal = 'I'
    var ans = 0
    for (s in ss!!) {
        if(s == expectedVal){
            validStrLen++
            if(validStrLen == (2 * n + 1)){
                validStrLen -= 2
                ans += 1
            }
            expectedVal = if (expectedVal == 'I') 'O' else 'I'  
        } 
        else if(s == 'O'){
            validStrLen = 0
        }
        else if(s == 'I'){
            validStrLen = 1
        }
    }
    println(ans)
}