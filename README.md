# Basic Calculator

### What is Python?
Python is a real quick programming language, with _**dynamic typed**_, that supports _multiples programming paradigms_ as: _**procedural programming**_, _**functional programming**_ and _**object-oriented programming**_. It was created by Guido van Rossun, in 1991, and his phillosophy emphasizes __*code redability*__.

>Learn more about Python here: ![Link to Python Documentation](https://www.python.org/doc/)

### What is Basic Calculator?
The _Basic Calculator_ project is a simple project, made in Python, that realizes the _four basic operations of math_: _**Addition**_, _**Subtraction**_, _**Multiplication**_ and _**Division**_.

### How it works?
It's quite simple! The project have two directories: `functions` and `validation`. When the user executes the `start.py` file, he will choose an option from the menu. The algorithm will send the user input to the `menu_validation` method, that will validate the option and will attribute the class of the operation choosen to the object `operation`, according to what operation the user choosed.

### How do I use the Basic Calculator?
Just clone the `basic-calculator-in-python` repository, run the `start.py`, choose an option from the menu and input two numbers.

### Requirements
To run the _Basic Calculator_, you will need the `Python 3.8.1`. The project doesn't has been tested in the other `Python` versions.

### Classes and Methods
- Operation
  - Addition

  - Subtraction

  - Multiplication

  - Division
    - Each `Operation` class has an method called `result`, which returns the result between the two numbers typed by the user. Also, each `Operation` class inherits the `Base` class, which provides methods as `setX` and `setY`, that is responsible to set values to the numbers that will be used in the math operations.

- Base
  - `__init__`
    - The `__init__` method initializes the `Operation` class with default values that will be used in the operation if the user doesn't type values to the `x` and `y` variables. By default, `__init__` method initializes the `x` and `y` variables with `0` and `1` values, respectively. Also, `__init__` method allows to use the `x` and `y` variables with the `self` parameter.

  - `setX`
    - The `setX` method receives the first typed number by the user, which can be an `Integer` or an `Float` number, and replaces the default value of `x` attribute by the typed number value.

  - `getX`
    - The `getX` method returns the value of `x` attribute, which can be the default value or the value of the typed number by the user. 

  - `setY`
    - The `setY` method receives the second typed number by the user, which can be an `Integer` or an `Float` number, and replaces the default value of `y` attribute by the typed number value.

  - `getY`
    - The `getY` method returns the value of `Y` attribute, which can be the default value or the value of the typed number by the user.

- Menu
  - `process_validation`
    - The `process_validation` method receives an input from the user. It is used to validate if the user wants to run the algorithm or not. If the `process_validation` receives 'S' as argument, the algorithm will execute.

  - `show_menu`
    - The `show_menu` method shows the options of operations that the user can choose.

  - `option_validation`
    - The `option_validation` method receives the choosed option by the user as argument.

  - `load_values`
    - The `load_values` method is responsible to read the two typed numbers by the user. Also, this method receives the `operation` as parameter, which allows to set the `x` and `y` attributes values as the typed numbers by the user and to show the result of the `operation`.
