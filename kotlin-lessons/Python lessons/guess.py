from not_equal import not_equal_to_two

def guess_game(x, init, number_of_tries):
    while init < number_of_tries:

        if x == 100:    
            print("Correct")
            break
        elif x >= 101:
            print("Try lower")
            not_equal_to_two(init)
        elif x <= 99:
            print("Try higher")
            not_equal_to_two(init)
      
        init += 1 
