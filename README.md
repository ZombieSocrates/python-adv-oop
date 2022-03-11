# python-adv-oop
Code work for _Udemy: Python OOP with 10 Real-World Programs_. Files for this course located [here.](https://github.com/pythonprocourse/files)


# structure
There is a separate directory for each of the 10 programs, each with its own `requirements.txt` and virtualenv.

## project one setup and demo
**Geometry Game:** A miniature CLI game that generates a random rectangle, asks the user to guess _a point within the rectangle._ If the user's guess falls within the rectangle, we also ask her or him to guess the _area of the rectangle._ Finally, the random rectangle and the point the user guessed is displayed on a canvas using python's built-in [turtle graphics module](https://docs.python.org/3/library/turtle.html).

```
cd geometry-game
pyenv virtualev 3.8.2 geometry-game
pyenv activate geometry-game
python game.py
```

## project two setup and demo
**Bill Sharing Report:** A CLI tool that helps roommates pay for a shared bill proportionally according to how many days in a given month they were present during the expense period. The tool solicits information about the bill and gathers names and days of residency for each of the users. Once it has this information, it creates a PDF summary of the shared costs using [python's port of the FPDF utility](https://pypi.org/project/fpdf/), saves it to the `bill_sharing` directory, and optionally opens the PDF report in a browser.

```
cd bill-sharing
pyenv virtualenv 3.8.2 bill-sharing
pyenv activate bill-sharing
pip install -r requirements.txt
pythom demo.py	
```

## project two setup and demo
**math painter**: Draw squares and rectangles on a canvas by entering numbers in the command line. Generates an output impage at the end of it all.


```
cd math-painter
pyenv virtualenv 3.8.2 math-painter
pyenv acticvate math-painter
pip install -r requirements.txt
python main.py
```

