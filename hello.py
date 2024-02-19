# write a program that predicts the future time
from random import randint
num = 3
ahead = 7


if (num + ahead > 12):
    future = (num + ahead) % 12
    print("That will be ", future, "pm", sep="")
else:
    print("That will be ", num + ahead, "am", sep="")

