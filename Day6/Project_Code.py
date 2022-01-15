def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()    
        if wall_on_right() and not front_is_clear():
            turn_left()  
    elif front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
       
