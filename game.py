
from kivy.uix.layout import Layout

from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label

from kivy.uix.image import Image

from kivy.uix.behaviors import ButtonBehavior

from kivy.uix.button import Button

from kivy.app import App

import random

from kivy.core.window import Window



class Game(Layout):

    def __init__(self, **kwargs):

        Layout.__init__(self,**kwargs)

        t = "title.jpg"

        title = Imb(t, 50, 100)

        title.x = 250

        title.y = 400

        self.countA = 0

        self.countB = 0

        self.l1 = Label()
        self.l2 = Label()

        self.add_widget(title)

        self.bt = Button(text='next round!', font_size = 18)

        self.bt.bind(on_press = self.nextRound)

        self.add_widget(self.bt)






    def nextRound(self, x):

        rock = "rock.jpg"

        paper = "paper.jpg"

        scissors = "scissors.jpg"

        im1 = Imb(rock, 300, 300)

        im2 = Imb(paper, 300, 300)

        im3 = Imb(scissors, 300, 300)

        im4 = Imb(rock, 300, 300)

        im5 = Imb(paper, 300, 300)

        im6 = Imb(scissors, 300, 300)

        rnd1 = [im1, im2, im3]
        rnd2 = [im4, im5, im6]

        num1 = random.randint(0, 2)

        num2 = random.randint(0, 2)

        player1 = rnd1[num1]

        player2 = rnd2[num2]


        player1.x = 100

        player1.y = 200

        player2.x = 500

        player2.y = 200

        self.add_widget(player1)

        self.add_widget(player2)

        dic = ["Rock", "Paper", "Scissors"]


        self.winRound(dic[num1],dic[num2])





    def winRound (self, player1, player2):




        if player1 == "Rock" and player2 == "Scissors":
            self.countA=self.countA+1
        elif player1 == "Paper" and player2 == "Rock":
            self.countA = self.countA + 1
        elif player1 == "Scissors" and player2 == "Paper":
            self.countA = self.countA + 1
        elif player1 == "Rock" and player2 == "Paper":
            self.countB = self.countB + 1
        elif player1 == "Paper" and player2 == "Scissors":
            self.countB = self.countB + 1
        elif player1 == "Scissors" and player2 == "Rock":
            self.countB = self.countB + 1

        if self.countA==3:
            l = Label(text="Player 1 has won!!!", font_size=20)

            l.x = 350

            l.y = 350

            self.add_widget(l)
            self.remove_widget(self.bt)

        if self.countB == 3:
            l = Label(text="Player 2 has won!!!", font_size=20)

            l.x = 350

            l.y = 350

            self.add_widget(l)
            self.remove_widget(self.bt)


        l1 = Label(text=str(self.countA))

        l1.x = 0

        l1.y = 250

        l2 = Label(text=str(self.countB))

        l2.x = 700

        l2.y = 250

        self.remove_widget(self.l1)
        self.remove_widget(self.l2)

        self.add_widget(l1)
        self.add_widget(l2)

        self.l1 = l1
        self.l2 = l2



class Imb(ButtonBehavior, Image):

    def __init__(self,myImg,x1,y1):

        ButtonBehavior.__init__(self)

        Image.__init__(self)

        self.source = myImg

        self.x=x1

        self.y=y1

        self.width  = self.width + 100

        self.height = self.height + 100





class TestApp(App):

    def build(self):

        Window.clearcolor = (0, 0.3, 0, 1)

        self.title = 'based graphics'

        return Game()





TestApp().run()

