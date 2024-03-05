# closure is the function having access to scope of its parent function 
# after the parent function has returned


def parent_function(user,coins):
    # coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n"+ user +"has" + str(coins) + "coins left.")
        elif coins ==1:
            print("\n"+ user + "has" + str(coins) + "coins left.")
        else:
            print("\n" + user +"is out of coins.")
    return play_game
David = parent_function("David",4)
Victoria = parent_function("Victoria",7)


David()
David()


Victoria()


David( )
            