import turtle
lineLength = float(input("What length line would you like? "))

while lineLength > 0 :
    print("You have choosen to draw a shape, please enter specifics:")
    penColor = input("Please choose a pen color: ")
    shape = input("which shape would you like to draw? ")

while shape.lower() not in ["octagon", "heptagon", "hexagon"] :
    print("You have to select a shape from the specified list.")
    shape = input("What shape would you like to draw: ")