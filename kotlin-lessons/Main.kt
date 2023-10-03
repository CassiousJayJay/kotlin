fun main(){  
      var item1 = Item("laptop", 2500, 2)
    println(item1.quantity)

    var item2 = Item("iphone 7", 5000, 7)
     var price_return = item2.calculate_total_price(item2.price, item2.quantity )
    println(price_return)
    
}

class Item(var name: String, var price: Int, var quantity: Int){
constructor (): Item{
    
}

    fun calculate_total_price(x: Int, y: Int): Int {
        return x * y
    }

}