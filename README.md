# Trivia
This is a Python implementation of a trivia game using the tkinter library for the graphical user interface (GUI).

## Requirements
This program requires Python 3 to run. No additional dependencies are required.

## Usage

Once the program is running, a window will pop up with a banner that displays the name of the game, as well as a dropdown menu with a list of genres to choose from. You can select a genre from the list and click the "NEXT" button to begin playing the game. If the option chosen is "Random selection", a genre is randomly selected.

The questions are stored in CSV files, with one file for each genre. The CSV files contain columns for the question, the possible options, and the correct answer. The csv module is used to read the CSV files into a list of lists.

When the game starts, a question will be displayed with possible options to choose from. Select the option that you think is correct and click the "CHECK" button. If you are correct, your score will be incremented and the next question will be displayed. If you are incorrect, you will be given the correct answer and the next question will be displayed.

If you click the "NEXT" button without selecting an option, the question will be marked as "Not attempted".

You can exit the game at any time by clicking the "QUIT" button. If you attempt to close the window using the "X" button, a message box will appear asking you to confirm that you want to quit the game.

## Sample Usage

The given example code is located at the bottom of the file and therefore, will run if you run the script [trivia.py](https://github.com/Suhana66/Trivia/blob/master/trivia.py). To run the script [trivia.py](https://github.com/Suhana66/Trivia/blob/master/trivia.py), use the command `python3 trivia.py`.

```python
if __name__ == "__main__":
    Trivia(
        "TriviaQ&A",        # game title
        "600x500",          # game geometry
        "Cochin",           # font style
        16,                 # font sizing, spacing
        (
            "#FFFFFF",      # light color
            "#E5E5E5",      # medium color
            "#000000",      # dark color
            "#00B232",      # 'correct' color
            "#B20000"       # 'incorrect' color
        ),
        "categories(csv)"   # path to directory containing questions
    )
```

## License
The code in this repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The trivia data used by this project is adapted from the [OpenTriviaQA](https://github.com/uberspot/OpenTriviaQA), repository which is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). Please note that this license applies only to the trivia data and not to the code in this repository. If you plan to use the trivia data in your own project, you must comply with the terms of the Creative Commons Attribution-ShareAlike 4.0 International License.
