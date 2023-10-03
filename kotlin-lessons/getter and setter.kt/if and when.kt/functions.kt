fun main() {
    println(sum(20, 40, 30, 20, 16, 49, 29))
    val y = {a: Int, b: Int -> a * b}
    {}
}

fun sum(vararg x: Int): Int{
    var sum = 0
    for(i in x){
        sum = sum + 1
    
    }
    return sum
}
fun drawBox(){
    for(i in 1..10){  
        print("*")
    }
    print("\n")
    for(i in 1..2){
        print("*")
    }
    for(j in 1..8){
        print("")
    }

}