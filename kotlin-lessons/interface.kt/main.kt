fun main() {
    val left: Button = Button()
    left.click()
    val mouse: Cursor = Cursor()
    mouse.click()
    mouse.showoff()
}

interface Clickable {
fun click()
fun showoff() {
println("Am here")
}
}

class Button: Clickable{
    override fun click() {
        println("clicked")
    }
}
class Cursor: Clickable{
    override fun click() {
        println("Cursor clicked")
    }
    override fun showoff()
    println("Am here")
}
fun left() {
    println("Left was pressed")
}


