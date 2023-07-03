from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Just stop the animations of movements
screen.tracer(0)

# tim = Turtle("square")
# tim.color("white")
# tim.turtlesize(stretch_wid=1, stretch_len=-3)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Right", fun=snake.turn_east)
screen.onkey(key="Down", fun=snake.turn_south)

game_is_on = True
while game_is_on:
    # We update the screen, restart the animations and then wait 0.2 sec with sleep()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail, ignore the head with slicing [1:]
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
