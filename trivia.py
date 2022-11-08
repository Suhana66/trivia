import tkinter
from tkinter import messagebox
import csv
import random
import os

class Trivia():
    
    def __init__(self, title: str, geometry: str, font: str, em: int, colors: tuple, dir: str) -> None:
        assert os.path.isdir(dir), "Invalid dir path"

        # initialization of gui window
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.configure(background = colors[0])
        self.window.geometry(geometry)
        self.window.update()    # used to get the correct winfo_width()

        # STYLE ATTRIBUTES

        # (light color, medium color, dark color, correct color, incorrect color)
        self.colors = colors

        # for sizing
        self.em = em

        # (font style, font size)
        self.font = (font, self.em)

        # PRACTICAL ATTRIBUTES

        # the directory path that contains the questions for the game
        self.dir = dir

        # array of genres to choose from for questions
        self.categories = []
        for file in os.listdir(self.dir):
            path = os.path.splitext(file)
            if path[1] == ".csv": self.categories.append(path[0].capitalize().replace("-", " "))
        
        # IntVar is a class whose instance stores integer data
        # its value on the screen changes, when the value of the variable is changed (using setter method)

        # initializing a variable to hold the current question number, value = 0
        self.q_no = tkinter.IntVar()

        # initializing a widget to hold the current question (text is set in a method later)
        self.question = tkinter.Message(
            master = self.window,
            font = self.font,
            foreground = self.colors[2],
            background = self.colors[0],
            justify = tkinter.LEFT,
            width = self.window.winfo_width() - self.em * 5
        )

        # initializing a tkinter variable to hold the selected option number, value = 0
        self.selected_option = tkinter.IntVar()

        # added a trace to tkinter variable (run callback function every time variable is changed)
        self.selected_option.trace_add("write", lambda var, blank, mode, self = self: self.next.configure(text = ("CHECK" if self.selected_option.get() else None)))

        # initializing an array of widgets to hold the possible options of the current question (a, b, c, d) (text is set in a method later)
        self.options = [tkinter.Radiobutton(
            master = self.window,
            text = "",
            variable = self.selected_option,
            value = i + 1,
            foreground = self.colors[2],
            background = self.colors[0],
            font = self.font,
            justify = tkinter.LEFT,
            wraplength = self.window.winfo_width() - self.em * 3
        ) for i in range(4)]

        # creating an object attribute containing the genre the user, self.category = random.choice(self.categories)
        self.set_category()

        # packing a widget to the top of the screen saying the name of the game
        self.banner(title)
        
        # display a dropdown menu where the genre of questions is selected
        self.dropdown = self.display_selection()

        # display the buttons required to play the game
        self.display_btns()

        # variables to keep track of the statistics of the game
        # self.streaks is an array of integers, needed to calculate the maximum streak earned by the player
        self.correct = 0
        self.attempted = 0
        self.streak = 0
        self.streaks = []

        # window close event handler
        self.window.protocol("WM_DELETE_WINDOW", self.display_msg)

        # mainloop() is a method that runs an infinte loop required to handle events in the gui
        # it continuously updates the gui window
        self.window.mainloop()


    # to pack a widget at the top of the screen with some text
    def banner(self, txt: str, reverse = False) -> tkinter.Label:
        fg, bg = self.colors[2], self.colors[1]
        if reverse: fg, bg = bg, fg
        banner = tkinter.Label(textvariable = txt) if getattr(txt, "__module__", None) == "tkinter" else tkinter.Label(text = txt)
        banner.configure(background = bg, foreground = fg, font = self.font)
        banner.pack(fill = tkinter.X, ipady = self.em // 10)
        return banner


    # setting the genre of the questions to be asked
    def set_category(self, value = None) -> str | None:
        self.category = random.choice(self.categories) if not value or value.lower().startswith("random") else value


    # setting self.csv to the array of questions (strings) that can be asked depending on self.category
    def set_csv(self) -> None:
        with open(f"{self.dir}/{self.category.replace(' ', '-')}.csv") as f:
            reader = csv.reader(f)
            next(reader, None)      # skip header of csv file
            self.csv = list(reader)


    # asking the next question to the user (reset)
    def set_question(self) -> None:

        # increment question number
        self.q_no.set(self.q_no.get() + 1)

        # reset selected option
        self.selected_option.set(0)

        # reset banner displaying question status
        self.status.configure(text = "NOT ATTEMPTED", foreground = self.colors[1], background = self.colors[2])
        
        # change question
        q = self.csv[self.q_no.get() - 1]
        self.question.configure(text = q[1])
        
        # change possible answers of question
        for i, op, in enumerate(self.options):
            if q[i + 3]: op.configure(text = q[i + 3], foreground = self.colors[2])
            else: op.pack_forget()


    # display the home page of the gui
    def display_selection(self) -> tkinter.OptionMenu:
        
        # display a dropdown for the user to choose the genre of the questions asked
        categories = ["Random selection"] + self.categories
        variable = tkinter.StringVar(self.window, categories[0])
        dropdown = tkinter.OptionMenu(self.window, variable, *categories, command = self.set_category)
        dropdown.configure(font = self.font, foreground = self.colors[2], background = self.colors[0])
        dropdown.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        return dropdown


    # function to instantiate a button in gui with common attributes
    def btn(self, txt: str, func) -> tkinter.Button:
        return tkinter.Button(
            master = self.window,
            text = txt,
            command = func,
            bd  = 0,
            font = self.font
        )


    # display all the buttons required in the gui =>
    # 1) create buttons using btn() method
    # 2) display tkinter.Button using place() method
    def display_btns(self) -> None:
        self.btn("CLEAR", lambda self = self: self.selected_option.set(0)).place(relx = 0.5, rely = 0.9, anchor = tkinter.E)
        self.next = self.btn("NEXT", self.next_btn)
        self.next.place(relx = 0.5, rely = 0.9, anchor = tkinter.W)
        self.btn("QUIT", self.display_msg).place(relx = 1, rely = 0, anchor = tkinter.NE)


    # calculate the statistics of the game after a question is answered
    def display_result(self) -> bool:

        # q -> str, get the question string
        q = self.csv[self.q_no.get() - 1]
        
        # op -> int, get the selected option
        op = self.selected_option.get()

        # correct -> bool, if correct option was selected
        correct = True if q[op + 2] == q[2] else False

        # color -> str (hexadecimal), the color that the option should be changed to
        color = self.colors[3 if correct else 4]

        # self.status -> banner (tkinter.Label)
        # if op and self.status["background"] == color -> if banner already displays result (stats already counted)
        # if not op -> question not attempted
        # return True -> the gui window needs to be updated
        if op and self.status["background"] == color or not op: return True

        # next() is a built-in function that returns the next item in an iterator
        # Here, next() returns the tkinter.Radiobutton that is the CORRECT OPTION and changes text color to 'correct' color
        next(op for op in self.options if op["text"] == q[2]).configure(foreground = self.colors[3])
        
        # change the text color of the SELECTED OPTION to 'correct' or 'incorrect' color
        self.options[op - 1].configure(foreground = color)

        # change the text of the banner that displays the status of the question
        self.status.configure(text = "CORRECT" if correct else "INCORRECT", foreground = self.colors[2], background = color)
        
        # incrementing the relevant stats
        if correct:
            self.correct += 1
            self.streak += 1
        else:
            self.streaks.append(self.streak)
            self.streak = 0
        self.attempted += 1

        # the gui window does not need to be updated
        return False
        

    # function called to quit the game
    # if the game is not started (self.q_no.get == 0), do not display messagebox, just quit
    # else, display stats of game, then quit
    def display_msg(self) -> None:
        if self.q_no.get(): messagebox.showinfo("Result",
            f"""Number of questions attempted: {self.attempted}\n
            Number of questions not attempted: {self.q_no.get() - self.attempted}\n
            Number of correct answers: {self.correct}\n
            Number of incorrect answers: {self.attempted - self.correct}\n
            Score: {self.correct / self.q_no.get() * 100}%\n
            Maximum Streak: {max(self.streaks, default=0)}""")
        self.window.destroy()


    # function called if the NEXT button is clicked
    def next_btn(self) -> None:
        
        self.next.configure(text = "NEXT")

        # if the game is not started and the next button is pressed, display the first question
        if not self.q_no.get(): self.initiate_question()

        # if the gui window needs to be updated
        if self.display_result():

            # if all questions have been exhausted, quit game
            if self.q_no.get() == len(self.csv): self.display_msg()
            
            # else, ask next question
            else: self.set_question()


    # display the first question (only the text is changed in subsequent questions)
    def initiate_question(self) -> None:

        # at this moment, genre of questions is selected, so hide dropdown menu
        self.dropdown.place_forget()

        # creating a banner displaying the genre selected and display it on the screen
        self.banner(self.category, True)

        # creating a banner displaying the current question number (updated using IntVar)
        self.banner(self.q_no)

        # reading the csv file to get the questions of the genre specified
        self.set_csv()

        # creating a banner displaying the status of each question (not attempted/correct/incorrect)
        self.status = self.banner("NOT ATTEMPTED", True)

        # displaying the current question text
        self.question.pack(anchor = tkinter.W, pady = self.em // 4, padx = self.em * 2)

        # displaying the possible answers to the current question
        for op in self.options: op.pack(anchor = tkinter.W, padx = self.em * 1.8, pady = self.em // 4)


# example of how the Trivia class is used
if __name__ == "__main__":
    Trivia("TriviaQ&A", "600x500", "Cochin", 16, ("#FFFFFF", "#E5E5E5", "#000000", "#00B232", "#B20000"), "categories(csv)")
