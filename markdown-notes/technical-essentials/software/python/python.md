# Python

- Coding in Python notes

## Index

- [Index](#index)
- [C vs Python](#c-vs-python)
- [Comments](#comments)
- [Constants](#constants)
- [Default Parameters](#default-parameters)
- [HEX Integers](#hex-integers)
- [Memory Optimization](#memory-optimization)
- [PEP 8](#pep-8)

## C vs Python

- Private vs public
  - Functions can’t be specified as private for file scope only
  - You either import an entire file, a module in a file, or nothing
  - Can’t import a file without also importing all the global functions
- Function prototypes
  - Doesn’t exist
- Explicit integer data types
  - Doesn’t exist unless you import a library
- Data type specification at function declaration
  - Doesn’t exist, but you can add “type hints” that help the user see what data types each variable is supposed to be
  - Annoying for functions that return multiple data

## Comments

- Block comments written w/ docstrings, single-line comments written w/ “#”

## Constants

- Constants are differentiated from global variables w/ capitalization where all caps = constant, but they’re all essentially global variables

## Default Parameters

- When creating a new instance of a class, all parameters indicated in the signature of the constructor definition must be provided UNLESS the parameters have default values
- This serves as a shorthand way of implementing “overloading” concept as well, but there’s a catch when you assign default values to mutable parameters (noted below in “memory optimization in Python”)

## HEX Integers

- Python supports 0x for HEX representation

## Memory Optimization

- Python’s memory optimization is great for efficient memory allocation and reuse for mutable data
- Side effects include all instances of a class sharing the same mutable variable when a mutable variable is declared and assigned in the signature of a method
- The solution to this is to assign mutable variables “None”, an immutable singleton object (the singleton class is for when there should only ever be a single instance of said class)

## PEP 8

- “Python enhancement proposal”
- A style guide for writing readable and consistent Python code, including:
  - Indentation
    - 4 spaces per indentation
  - Max line length
    - 79 char limit
    - Additional 72 char limit for comments/docstrings
  - Blank lines
    - 2 blank lines between functions (not in class) and classes,
    - 1 blank line between methods in a class
  - Imports
    - Top of the file in order of:
      - Standard library imports
      - Related third-party imports
      - Local app/library-specific imports
  - Whitespace in expressions & statements
    - Avoid unnecessary spaces in parenthesis, brackets, braces
    - Don’t use spaces when indicating keywords or default values
  - Comments
    - Explain why things are done, not what’s done
    - Write in complete sentences
    - Put a space after “#” for the comment
  - Naming conventions
    - Function names, variable names, file names should be snake case (all lower)
    - Class names should be camel case (start w/ upper)
    - Constants are all upper w/ underscores
  - Docstrings
    - Should describe purpose of functions, classes, and modules
    - Eh just follow sphinx lol
  - Comparisons
    - Use “is” or “is not” when comparing “None” or Boolean values
