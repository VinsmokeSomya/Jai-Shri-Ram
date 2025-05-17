#By - VinsmokeSomya 

# Import the turtle module for graphics
from turtle import* 

# Set the window title
title('Jai Shree Ram')
# Set the background color of the window
bgcolor('black')
# Set the pen size for drawing
pensize(6)
# Set the pen color
pencolor("orange")

# Create a list of strings "जय श्री राम"
Ram_naam = ["जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम","जय श्री राम","जय श्री राम",
"जय श्री राम","जय श्री राम"]

# Calculate the angle for each text segment to form a circle
angle = 360/49
# Lift the pen to move without drawing
penup()
# Set the initial y-coordinate for the circular text
sety(-1)
# Loop to write the text in a circle
for i in range(50):
    left(angle)
    forward(260)
    # Write the text
    write(Ram_naam[i], align="right",
    font=('Arial',12,"bold"))
    # Move back to the center
    backward(260)

# Lift the pen to move to the center for the next text
penup()    
# Move the turtle to the center position
goto(-40,-20)
# Put the pen down to start drawing again
pendown()
# Write "|| राम ||" in the center
write("|| राम ||", font=("Arial", 60,
"normal"), align="center")
# Hide the turtle cursor
hideturtle()
# Keep the window open until it's manually closed
done()
