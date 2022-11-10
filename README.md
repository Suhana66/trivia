# Trivia

A python script to create a graphical user interface to play trivia.


## Concepts learnt

1. Object Oriented Programming
2. Tkinter Library in Python
3. CSV File Handling in Python


## Requirements

Tkinter is the only GUI framework built into the Python standard library. Therefore, if python is installed on the device, no other installations are required to run the script [trivia.py](https://github.com/Suhana66/Trivia/blob/master/trivia.py).


## Usage

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

All files in the directory [categories(csv)](https://github.com/Suhana66/trivia/tree/master/categories(csv)) is adapted from the the following repository- https://github.com/uberspot/OpenTriviaQA licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

The python script [trivia.py](https://github.com/Suhana66/Trivia/blob/master/trivia.py) is under [MIT License](https://choosealicense.com/licenses/mit/).
