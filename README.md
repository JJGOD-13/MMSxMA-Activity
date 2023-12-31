# MMSxMA-Activity
The importable python file that will be used to contain the code that is required to run the MA activity

# How it works

This repository contains mainly the MMScar file that contains a list of importable functions that you can use in order to control the MA activity car sets. The module is built using the Pymata4 library in order to interface with Arduino UNO.

# Before you begin

You need to have a couple of things already installed on the computer.
Run the following commands in your terminal.

```bash
pip install pymata4
```
>You might have to replace `pip` with `pip3` depending on the version installed on the computer.

You will also need to clone into the github repository in order to access the files required.

```bash
git clone https://github.com/JJGOD-13/MMSxMA-Activity.git
```

This will clone the files into your current working directory.

 ***You will also have to install VScode on the computer.***

You can do this by going to the website and installing from there

# Getting Started
 
**Once you've cloned into the repository, simply open `car.py` and start coding.**

# A quick rundown of Python

**Python is a programming language that is beginner friendly. Here is simple syntax to get you started.**

 Variables can be set using the following syntax

 ```python
 variable = number
 ```
 > In Python is usefull to think of the '=' sign as "is set to" rather than mathematical equivalence.

 You can use the print statement to show things on the terminal.
 ```python
 print("Hello World")
 ```

<br>
Python like all other programming languages supports datatypes

some common ones are 

- **Integers and Floats**
  - These act just like normal numbers.
  - You can perform all the normal numeric operations on them such as addition, multiplication division and subtraction etc.
  - Use `int()` or `float()` to explicitly turn something into a number.
  
> ⚠️ Warning
> 
> If you try to turn anything other than a number into an int or float. You will cause an error.

- **Strings**
  - Strings can be thought of as characters or sentences.
  - All variables that you want to store as strings must be enclosed with `""`.
  - Adding strings with the `+` sign will actually stitch them together. For example: 
  ```python
  x = "hello"
  y = "world"

  x + y
  ```
  Will output `helloworld`. It's handy to keep this in mind when debugging your code.

  # Comments.
  If you want to write something in your document with it being ignored by Python simply type a `#` before the line. For example:
  ```python
  # This line will be ignored.
  ```

  ## Loops

  There are many different ways to make loops in Python.
  The ones you'll be using are `while` and `for` loops.

  ### `while` loops
  ```python
  while True:
    # Code you want to run
  ```
  This code will run forever until you manually stop it. So use it wisely.
