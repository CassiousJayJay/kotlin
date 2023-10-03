fun main() {
val house = House(4, 5.5, "red", 500)
house.simpleprompt()
house.mediumprompt(false)

}
class House ( colour:String, rooms: Int){
    var colour: String
    var rooms: Int
    init {
        this.colour = colour
        println(this.colour)
    }
    init {
        this.rooms = rooms
        println(this.rooms)
    }
    constructor(rooms:Int, bathrooms: Double, colour: String):this (colour, rooms) {
    println("Colour: $colour")
}

constructor(rooms:Int, bathrooms: Double, colour: String, rates:Int):this (colour, rooms,) {
    println("Rates: $rates")
}
fun simpleprompt() {
    println("The colour of the house is: $colour and the amount of rooms is: $rooms")
}
fun mediumprompt(includespool: Boolean) {
    println("The colour of the house is: $colour and the amount of rooms is: $rooms and includes pool: $includespool")
}
}