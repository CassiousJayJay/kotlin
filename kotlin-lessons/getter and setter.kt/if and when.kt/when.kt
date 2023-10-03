fun main() {
   //sum()
   pyramid()

}

fun sum() {
print("Enter numbers:")
    var num = readln().toInt() 
    var sum = 0
while (num != 0) {
    sum += num 
     print("Enter another number")
    num = readln().toInt()
}
    println("sum: $sum")
}
fun pyramid() {
    for(i in 0..5){
    for(j in 0..i) {
        print("#")
        }
        print("\n")
    }
}
fun game(){
    val secretNumber = 
}