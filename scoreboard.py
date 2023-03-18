from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(-20, 260)
        self.scores()

    def scores(self):
        self.clear()
        self.write(f"score : {self.score} High score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.scores()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.scores()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('white')
    #     self.clear()
    #     self.write(f"   Game over!\n Your score is : {self.score}", move=False, align=ALIGNMENT, font=FONT)
