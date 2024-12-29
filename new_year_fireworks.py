import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Happy New Year 2025 🎆")
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.tracer(0)

# Function to create a firework effect
def draw_firework(x, y, color):
    firework = turtle.Turtle()
    firework.speed(0)
    firework.color(color)
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    for _ in range(36):
        firework.forward(50)
        firework.backward(50)
        firework.right(10)
    firework.hideturtle()

# Function to display "Happy New Year 2025" message
def display_message():
    message = turtle.Turtle()
    message.speed(0)
    message.color("white")
    message.penup()
    message.hideturtle()
    message.goto(0, -100)
    message.write("Happy New Year 2025!", align="center", font=("Courier", 24, "bold"))

# Firework positions and colors
firework_positions = [(-200, 200), (0, 200), (200, 200), (-100, 50), (100, 50)]
firework_colors = ["red", "blue", "yellow", "green", "purple"]

# Animate the fireworks
for _ in range(3):
    for pos, color in zip(firework_positions, firework_colors):
        draw_firework(pos[0], pos[1], color)
        screen.update()
        time.sleep(0.5)

# Display the message
display_message()
screen.update()

# Wait for user to close the window
screen.mainloop()
