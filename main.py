import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("81 Cities of Turkey")
image = "image_tr.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("cities_of_turkey.csv")
all_cities = data["city"].to_list()
guessed_cities = []


while len(guessed_cities) < 81:
    answer = screen.textinput(title=f"{len(guessed_cities)}/81 Cities Correct",
                              prompt="What's another city's name?").title()

    if answer == "Exit":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        new_data = pd.DataFrame(missing_cities)
        new_data.to_csv('cities_to_learn.csv')
        break
    if answer in all_cities and answer not in guessed_cities:
        guessed_cities.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer]
        t.goto(int(city_data.x), int(city_data.y))
        t.write(answer)

screen.exitonclick()
