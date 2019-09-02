#>>>>>>>>>>>Module 1 - Turtle Exercise <<<<<<<<<<<<<<<<<<<
import turtle
my_turtle=turtle.Turtle()
my_turtle.color('blue')

#my_turtle.forward(1000)

#Making an uppercase W
my_turtle.goto(0,0)
my_turtle.right(90)
#if 'tail' is down, forward leaves a trail
#if 'tail is up, the foward command moves the cursor to a new location without any line
my_turtle.up()
my_turtle.backward(100)
my_turtle.down()
my_turtle.right(160)
my_turtle.backward(100)
my_turtle.right(40)
my_turtle.forward(50)
my_turtle.left(40)
my_turtle.backward(50)
my_turtle.right(40)
my_turtle.forward(100)
my_turtle.up()

#Making a lowercase o
my_turtle.color('green')
my_turtle.up()
my_turtle.goto(75,4)
my_turtle.right(-290)
#Moving forward double the radius of the circle
my_turtle.forward(50)
my_turtle.down()
my_turtle.circle(25, 360)
my_turtle.up()

#Making a lowercase w
my_turtle.color('red')
#Going to 75 plus a buffer of 10 for space between he characters
my_turtle.goto(160,4)
my_turtle.right(90)
my_turtle.up()
my_turtle.backward(50)
my_turtle.down()
my_turtle.right(160)
my_turtle.backward(50)
my_turtle.right(40)
my_turtle.forward(50)
my_turtle.left(40)
my_turtle.backward(50)
my_turtle.right(40)
my_turtle.forward(50)
my_turtle.up()


