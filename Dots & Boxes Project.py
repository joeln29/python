""""
Ohjelmointi 1, viikko 13 projekti: Dots & Boxes
Joel N & Eetu
"""
from tkinter import *


class Names:
    """
    Class which contains the input screen information and methods before the game
    """

    def __init__(self):
        """
        Constructor, initializes the newly created object.
        """
        # Create window where player names are typed
        self.__names = Tk()
        self.__names.title("Enter players names")
        self.__text = None
        self.__names.geometry("400x200")
        # Enter players names
        self.__player1 = Entry()
        self.__player2 = Entry()
        self.__player1_label = Label(self.__names, text="Player 1")
        self.__player2_label = Label(self.__names, text="Player 2")
        # Empty label, which shows error if too many characters is given (max 15)
        self.__tietoikkuna = Label(self.__names, text=self.__text)

        # The position of players names
        self.__player1_label.grid(row=1, column=1)
        self.__player1.grid(row=2, column=1)
        self.__player2_label.grid(row=1, column=2)
        self.__player2.grid(row=2, column=2)
        self.__tietoikkuna.grid(row=3, column=1)

        # Start the game self.button, which closes the input window and starts the game
        self.__start_ = Button(self.__names, text="Start", command=self.start_names)
        self.__start_.grid(row=1, column=3)

        # Quit self.button
        self.__quit_self = Button(self.__names, text="Quit", command=self.quit_names)
        self.__quit_self.grid(row=5, column=3)

        self.__varit = {}

        self.__names.mainloop()

    def quit_names(self):
        """
        When called, quits the program before the actual game
        :return: none
        """
        self.__names.destroy()

    def start_names(self):
        """
        Starts the mainloop (game)
        :return: none
        """
        a = str(self.__player1.get())
        b = str(self.__player2.get())
        # Check how many characters was given each player
        # if more than 15, clear windows and show error message

        if len(a) > 15 or len(b) > 15:
            self.__tietoikkuna.configure(text="The name has to have \n less than 15 characters!")
            self.__player1.delete(0, END)
            self.__player2.delete(0, END)

        # if zero characters were given, "print" error message as well
        elif len(a) == 0 or len(b) == 0:
            self.__tietoikkuna.configure(text="The names has to \n have characters!")
            self.__player1.delete(0, END)
            self.__player2.delete(0, END)

        else:
            self.__player1.configure(text=a)
            self.__player2.configure(text=b)
            self.__names.destroy()
            Game(a, b)


class Game:
    """
    This class contains all the necessary information regard to the game, and it's GUI. Players' names come from the
    class above
    """

    def __init__(self, player1, player2):
        """
        Constructor, initializes the newly created object.
        :param player1:
        :param player2:
        """
        # A list which determines if all four borders of a square are same color, and makes the center same color
        # This is also needed when calculating points
        self.__varit = []
        for a in range(11):
            temp = []
            for b in range(11):
                temp.append(0)
            self.__varit.append(temp)
        self.__player1 = player1
        self.__player2 = player2
        self.__vuoro = 0
        self.__turn = 0
        self.__pisteet = {"Player 1": 0, "Player 2": 0}
        self.__counter = 0

        # Create the game window
        self.__paaikkuna = Tk()

        # Size of the window
        self.__paaikkuna.geometry("500x350")
        self.__paaikkuna.title("Dots & Boxes")

        # Show player names in the upper left corner
        self.__player1_label = Label(text="Player 1: " + self.__player1).grid(row=1, column=15)
        self.__player2_label = Label(text="Player 2: " + self.__player2).grid(row=2, column=15)
        self.__pisteet_player1 = Label(text=f"Points: {self.__pisteet['Player 1']}")
        self.__pisteet_player1.grid(row=1, column=16)
        self.__pisteet_player2 = Label(text=f"Points: {self.__pisteet['Player 2']}")
        self.__pisteet_player2.grid(row=2, column=16)
        self.__restart_button = Button(text="Restart", command=self.restart_game).grid(row=20, column=21)

        # Label which tells who won the game
        self.__win = Label(text="")
        self.__win.grid(row=15, column=15)
        # Quit self.button
        self.__quit_button = Button(text="Quit", command=self.quit).grid(row=20, column=22)

        # Labels row 1
        self.label1 = Label(text="O", background="black")
        self.label1.grid(row=1, column=1)
        self.label2 = Label(text="O", background="black")
        self.label2.grid(row=1, column=3)
        self.label3 = Label(text="O", background="black")
        self.label3.grid(row=1, column=5)
        self.label4 = Label(text="O", background="black")
        self.label4.grid(row=1, column=7)
        self.label5 = Label(text="O", background="black")
        self.label5.grid(row=1, column=9)
        self.label6 = Label(text="O", background="black")
        self.label6.grid(row=1, column=11)

        # Labels row 3
        self.label7 = Label(text="O", background="black")
        self.label7.grid(row=3, column=1)
        self.label8 = Label(text="O", background="black")
        self.label8.grid(row=3, column=3)
        self.label9 = Label(text="O", background="black")
        self.label9.grid(row=3, column=5)
        self.label10 = Label(text="O", background="black")
        self.label10.grid(row=3, column=7)
        self.label11 = Label(text="O", background="black")
        self.label11.grid(row=3, column=9)
        self.label12 = Label(text="O", background="black")
        self.label12.grid(row=3, column=11)

        # Labels row 5
        self.label13 = Label(text="O", background="black")
        self.label13.grid(row=5, column=1)
        self.label14 = Label(text="O", background="black")
        self.label14.grid(row=5, column=3)
        self.label15 = Label(text="O", background="black")
        self.label15.grid(row=5, column=5)
        self.label16 = Label(text="O", background="black")
        self.label16.grid(row=5, column=7)
        self.label17 = Label(text="O", background="black")
        self.label17.grid(row=5, column=9)
        self.label18 = Label(text="O", background="black")
        self.label18.grid(row=5, column=11)

        # Labels row 7
        self.label19 = Label(text="O", background="black")
        self.label19.grid(row=7, column=1)
        self.label20 = Label(text="O", background="black")
        self.label20.grid(row=7, column=3)
        self.label21 = Label(text="O", background="black")
        self.label21.grid(row=7, column=5)
        self.label22 = Label(text="O", background="black")
        self.label22.grid(row=7, column=7)
        self.label23 = Label(text="O", background="black")
        self.label23.grid(row=7, column=9)
        self.label24 = Label(text="O", background="black")
        self.label24.grid(row=7, column=11)

        # Labels row 9
        self.label25 = Label(text="O", background="black")
        self.label25.grid(row=9, column=1)
        self.label26 = Label(text="O", background="black")
        self.label26.grid(row=9, column=3)
        self.label27 = Label(text="O", background="black")
        self.label27.grid(row=9, column=5)
        self.label28 = Label(text="O", background="black")
        self.label28.grid(row=9, column=7)
        self.label29 = Label(text="O", background="black")
        self.label29.grid(row=9, column=9)
        self.label30 = Label(text="O", background="black")
        self.label30.grid(row=9, column=11)

        # Labels row 11
        self.label31 = Label(text="O", background="black")
        self.label31.grid(row=11, column=1)
        self.label32 = Label(text="O", background="black")
        self.label32.grid(row=11, column=3)
        self.label33 = Label(text="O", background="black")
        self.label33.grid(row=11, column=5)
        self.label34 = Label(text="O", background="black")
        self.label34.grid(row=11, column=7)
        self.label35 = Label(text="O", background="black")
        self.label35.grid(row=11, column=9)
        self.label36 = Label(text="O", background="black")
        self.label36.grid(row=11, column=11)

        # Buttons
        self.__buttons = []
        for x in range(1, 12):
            for y in range(1, 12):
                if x % 2 == 0 and y % 2 == 1:

                    self.__buttons.append(Button(text="|", command=lambda x=x, y=y:self.button(x, y)))
                    self.__buttons[-1].grid(row=x, column=y)
                if x % 2 == 1 and y % 2 == 0:
                    self.__buttons.append(Button(text="---", command=lambda x=x, y=y: self.button(x, y)))
                    self.__buttons[-1].grid(row=x, column=y)

        # Squares which change color when borders around it have matching color
        self.__label1 = Label(text="", width=3)
        self.__label1.grid(row=2, column=2, )

        self.__label2 = Label(text="", width=3)
        self.__label2.grid(row=2, column=4, )

        self.__label3 = Label(text="", width=3)
        self.__label3.grid(row=2, column=6, )

        self.__label4 = Label(text="", width=3)
        self.__label4.grid(row=2, column=8, )

        self.__label5 = Label(text="", width=3)
        self.__label5.grid(row=2, column=10, )

        self.__label6 = Label(text="", width=3)
        self.__label6.grid(row=4, column=2, )

        self.__label7 = Label(text="", width=3)
        self.__label7.grid(row=4, column=4, )

        self.__label8 = Label(text="", width=3)
        self.__label8.grid(row=4, column=6, )

        self.__label9 = Label(text="", width=3)
        self.__label9.grid(row=4, column=8, )

        self.__label10 = Label(text="", width=3)
        self.__label10.grid(row=4, column=10, )

        self.__label11 = Label(text="", width=3)
        self.__label11.grid(row=6, column=2, )

        self.__label12 = Label(text="", width=3)
        self.__label12.grid(row=6, column=4, )

        self.__label13 = Label(text="", width=3)
        self.__label13.grid(row=6, column=6, )

        self.__label14 = Label(text="", width=3)
        self.__label14.grid(row=6, column=8, )

        self.__label15 = Label(text="", width=3)
        self.__label15.grid(row=6, column=10, )

        self.__label16 = Label(text="", width=3)
        self.__label16.grid(row=8, column=2, )

        self.__label17 = Label(text="", width=3)
        self.__label17.grid(row=8, column=4, )

        self.__label18 = Label(text="", width=3)
        self.__label18.grid(row=8, column=6, )

        self.__label19 = Label(text="", width=3)
        self.__label19.grid(row=8, column=8, )

        self.__label20 = Label(text="", width=3)
        self.__label20.grid(row=8, column=10, )

        self.__label21 = Label(text="", width=3)
        self.__label21.grid(row=10, column=2, )

        self.__label22 = Label(text="", width=3)
        self.__label22.grid(row=10, column=4, )

        self.__label23 = Label(text="", width=3)
        self.__label23.grid(row=10, column=6, )

        self.__label24 = Label(text="", width=3)
        self.__label24.grid(row=10, column=8, )

        self.__label25 = Label(text="", width=3)
        self.__label25.grid(row=10, column=10, )

        self.__paaikkuna.mainloop()

    def button(self, x, y):
        """
        Function which changes the buttons background color in the game
        :return: none
        """
        if x % 2 == 1:
            index = y//2 + (((x-1)//2)*11) - 1
        else:
            index = (((x-2)//2)*11) + (y-1)//2 + 5
        self.__vuoro += 1
        self.turn()
        if self.__turn == 0:
            self.__buttons[index].configure(bg="blue")
            self.__varit[x-1][y-1] = 1
        elif self.__turn == 1:
            self.__buttons[index].configure(bg="red")
            self.__varit[x-1][y-1] = 2
        self.check_labels(x-1, y-1)

    def quit(self):
        """
        When called, quits the game
        :return: none
        """
        self.__paaikkuna.destroy()

    def turn(self):
        """
        Determines whose turn it is
        :return: none
        """
        # If throw is an even number it's player 1 turn (red)
        if self.__vuoro % 2 == 0:
            self.__turn = 0

        # else throw is an odd number it's player 2 turn (blue)
        else:
            self.__turn = 1

    def game_over(self):
        """
        Tells who is the winner (or tie)
        :return: none
        """
        if self.__pisteet['Player 2'] == self.__pisteet["Player 1"]:
            self.__win.configure(text="It's a tie!")
        if self.__pisteet["Player 1"] > self.__pisteet['Player 2']:
            self.__win.configure(text=f"{self.__player1} wins!")
        if self.__pisteet['Player 2'] > self.__pisteet["Player 1"]:
            self.__win.configure(text=f"{self.__player2} wins!")

    def restart_game(self):
        """
        When called, restarts the game
        :return:
        """
        self.__paaikkuna.destroy()
        Game(self.__player1, self.__player2)

    def check_labels(self, x, y):
        """
        If all four borders of a square are the same color, make the square same color and give player a point
        :return: none
        """
        self.__counter += 1
        if x % 2 == 0:
            if x != 10:
                self.check_label(x + 1, y)
            if x != 0:
                self.check_label(x - 1, y)

        else:
            if y != 10:
                self.check_label(x, y + 1)
            if y != 0:
                self.check_label(x, y - 1)
        if self.__counter == 60:
            self.game_over()

    def check_label(self, x, y):
        """
        Checks if a square is won by a player
        :param x: int
        :param y: int
        :return: none
        """
        # Checks if all of the buttons around a square are from the same player
        if self.__varit[x + 1][y] == self.__varit[x - 1][y] == self.__varit[x][y + 1] == self.__varit[x][y - 1] \
                and self.__varit[x + 1][y] != 0:
            self.__varit[x][y] = self.__varit[x][y - 1]
            if self.__varit[x][y] == 2:
                Label(text="", width=3, bg="red").grid(row=x + 1, column=y + 1)
                self.__pisteet["Player 1"] += 1
                self.__pisteet_player1.configure(text=f"Points: {self.__pisteet['Player 1']}")

            else:
                Label(text="", width=3, bg="blue").grid(row=x + 1, column=y + 1)
                self.__pisteet["Player 2"] += 1
                self.__pisteet_player2.configure(text=f"Points: {self.__pisteet['Player 2']}")


def main():
    Names()


if __name__ == "__main__":
    main()
