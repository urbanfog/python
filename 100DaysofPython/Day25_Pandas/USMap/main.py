import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
state_list = df.State.to_list()
correct_answers = []
turd = turtle.Turtle()
turd.penup()
turd.hideturtle()

while len(correct_answers) < 50:
    answer_state = screen.textinput(
        title=f"Guess the State {len(correct_answers)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        state_data = df[df.State == answer_state]
        correct_answers.append(answer_state)
        name = state_data.State
        turd.goto(int(state_data.x), int(state_data.y))
        turd.write(state_data.State.item())


states_to_learn = []
for state in state_list:
    if not state in correct_answers:
        states_to_learn.append(state)
states_series = pandas.Series(states_to_learn, name="States to Learn")
states_series.to_csv("states_to_learn.csv")
