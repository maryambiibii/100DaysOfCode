#Solve Reeborg's World hurdles as an exercies

# Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdles_loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for hurdles in range(6):
    hurdles_loop()
    
# Hurdle 2

        
# Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdles_loop():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if not front_is_clear():
        hurdles_loop()
    else: 
        move()
        
# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdles_loop():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#position and number of hurdles  
while not at_goal():
    if not front_is_clear():
        hurdles_loop()
    else: 
        move()
        
