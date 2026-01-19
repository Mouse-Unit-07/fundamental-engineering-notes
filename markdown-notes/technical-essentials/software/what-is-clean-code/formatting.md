# Formatting

- Clean formatting notes
- Primarily from Robert C Martin's _Clean Code_

## Index

- [Index](#index)
- [Horizontal Formatting](#horizontal-formatting)
- [Vertical Formatting](#vertical-formatting)

## Horizontal Formatting

- **80 character rule**
  - The old 80 characters per line is pretty arbitrary- 100 to 120 is tolerable, but after that is just carelessness
  - Monitors are large now, and you can see a lot even without scrolling to the right, but if you’re making the font smaller on your text editor to view your code then you need to make some changes
- **Horizontal openness and density**
  - Use horizontal whitespaces to associate things that are strongly related, and disassociate things that aren’t
- **Horizontal alignment**
  - Don’t add extra whitespaces to align variable names, assignments, etc
  - This invites the reader to read just particular columns of text, and forces readers to go back and forth
  - The jagged lists won’t be a problem if the lists are short
- **Indentation**
  - Indentation aids readability- don’t remove them
  - Don’t collapse the indentation for short blocks of code (if statements, short while loops, etc)
- **Dummy scopes**
  - While and for statement blocks should be surrounded by braces and properly indented
  - A semicolon on the same line as the while loop expression is confusing- at the very least, the semicolon should be on its own line w/ indentation
- **Team rules**
  - Don’t mix individual styles- agree on a single coding standard

## Vertical Formatting

- **File size**
  - Complex systems can be created w/ a bunch of small files- 200 lines min to 500 lines max according to a study in _Clean Code_
  - Smaller files are easier to read than longer files
- **Newspaper metaphor**
  - At the top is the headline- you can decide whether to keep reading or not
  - As you continue downward, the details increase
- **Vertical openness between concepts**
  - Each blank line is a visual cue that identifies a new and separate concept
- **Vertical density**
  - Lines of code that are tightly related should appear vertically dense
  - Useless comments break the close association between variables, blocks of code, etc
- **Vertical distance**
  - Concepts that are closely related should exist close to each other, and in the same source file
  - There should be a good reason for separating related concepts into different files
  - Variable declaration
    - Should be as close to their usage as possible
    - W/ short functions, all variables should appear at the top of each function
  - Instance variables
    - Should be declared at the top of the class
    - The “scissors rule” might be applied in C++, placing instance variables at the bottom of the class
  - Dependent functions
    - If one function calls another, they should be vertically close and the caller should be above the callee if possible
  - Conceptual affinity
    - Certain bits of code want to be near other bits- this could be because of direct dependence, or maybe because the functions perform similar operations, etc
    - Group code that feel like they should be grouped together vertically close together
  - Vertical ordering
    - Function call dependencies should point in a downward direction only
    - Function called should be below those that call them
    - In C/C++ you can’t avoid function prototypes of helper private static functions- unavoidable, but keep the definitions below callers
