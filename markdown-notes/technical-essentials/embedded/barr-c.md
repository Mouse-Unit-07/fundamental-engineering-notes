# BARR-C

- BARR-C coding standard notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Aligning Code](#aligning-code)
- [Bad Assignment Location](#bad-assignment-location)
- [Bitfields](#bitfields)
- [C Version](#c-version)
- [Comma Operator](#comma-operator)
- [Comments](#comments)
- [Conditional Block Order](#conditional-block-order)
- [Constant Before Variable](#constant-before-variable)
- [Curly Brace](#curly-brace)
- [Floating Point](#floating-point)
- [Function Parenthesis and Spaces](#function-parenthesis-and-spaces)
- [Function-Like Macros](#function-like-macros)
- [Hardware Specific Features](#hardware-specific-features)
- [Header File Contents](#header-file-contents)
- [Hungarian Notation](#hungarian-notation)
- [Infinite Loops](#infinite-loops)
- [ISRs](#isrs)
- [Keywords to Avoid](#keywords-to-avoid)
- [Keywords to Use](#keywords-to-use)
- [LF Instead of CRLF](#lf-instead-of-crlf)
- [Line Width](#line-width)
- [Main Files](#main-files)
- [Multiple Return Statements](#multiple-return-statements)
- [Naming](#naming)
- [Nesting Levels](#nesting-levels)
- [Pointer Operators and Spaces](#pointer-operators-and-spaces)
- [Signed vs Unsigned](#signed-vs-unsigned)
- [Struct Union Padding](#struct-union-padding)
- [User Defined Types](#user-defined-types)
- [Variable Declaration Location](#variable-declaration-location)

## Overview

- > Barr Group's Embedded C Coding Standard was designed specifically to reduce the number of programming defects in embedded software. By following this coding standard, firmware developers not only reduce hazards to users and time spent in the debugging stage of their projects but also improve the maintainability and portability of their software.
  - _BARR-C:2018 Embedded C Coding Standard_
- BARR-C is a dated standard published after _Clean Code_
  - _Clean Code_ provides a better or equal standard w/ reasoning on all fronts
- All items mentioned in BARR-C but not mentioned in _Clean Code_, notable good practices agreeing w/ _Clean Code_, and bad practices enforced by BARR-C and countered by _Clean Code_ noted below

## Aligning Code

- Align variable names, `struct`/`union` members, assignment operators, etc
  - As _Clean Code_ describes, the left and right association becomes unclear when you align things
  - The effort should be to keep the set as small as possible, not to make a long list look tolerable

## Bad Assignment Location

- Don't make assignments in conditional statements or the controlling expression of loops

## Bitfields

- > Owing to differences across processor families and loose definitions in the ISO C language standards, there is a tremendous amount of implementation-defined behavior in the area of structures and unions. Bit-fields, in particular, suffer from severe portability problems, including the lack of a standard bit ordering and no official support for the fixed-width integer types they so often call out to be used with. The methods available to check the layout of such data structures include static assertions or other compile-time checks as well as the use of preprocessor directives, e.g., to select one of two competing struct layouts based on the compiler.
- ...Better yet, maybe just don't use them

## C Version

- Enforces C99
- BARR-C is aware of C90 / old ANSI-C's lack of explicit data types, useful data types like bool, etc

## Comma Operator

- Don't use the comma operator to declare multiple variables in one line

## Comments

- _Clean Code_ points out that comments are engineering failures, and that the failures come at a cost of heavy maintenance that can't be automatically checked for correctness
  - This holds true even after reading BARR-C, but below are notable points
- Casting comments
  - BARR-C enforces comments where data widths are assumed
  - ...The real solution if an architecture doesn't support a C99 compiler is to (unfortunately) reinvent the wheel and define custom types to replicate what `stdint.h` does, and then perform explicit casting
- C++ style single line comments are acceptable
  - Left to preference- comments are all failures
- Don't comment out code even temporarily- use `#if` conditional compilation instead
  - ...Code turned off w/ `#if`'s and commented out code are equally horrible in a codebase- make sure to commit neither
- > The number and length of individual comment blocks shall be proportional to the complexity of the code they describe
  - Again, comments are failures
  - If it's a necessary evil, then keep it minimum and short
- Write JavaDoc comments for Doxygen
  - Outdated- do this just when you absolutely have to (so for public facing API's)
- `WARNING:` for risks in changing code
  - Good if deemed a necessary evil
- `NOTE:` for why something is done
  - No need to use `NOTE:`- just write the comment
- `TODO:` for work-in-progress code
  - Good if deemed a necessary evil

## Conditional Block Order

- Prefer to show the shortest conditional statements and their associated blocks first
  - _Clean Code_ doesn't mention a preference, but code should be in the most readability friendly way- minimize jumping around

## Constant Before Variable

- Having the constant as the left operand of an equality operator helps catch bugs where you put down `=` instead of `==`
  - A decent idea, but impedes readability in exchange for behavior verification
  - Behavior verification should be done w/ TDD- readability has priority

## Curly Brace

- Opening curly braces should be on their own line, and same for the closing
- _Clean Code_ describes that this is preference too- it doesn't matter as long as you're consistent

## Floating Point

- Avoid using floating point whenever possible- use fixed point instead

## Function Parenthesis and Spaces

- Left and right parenthesis of a function call operator should never have surrounding spaces, but there should be a single space after the function name and the left parenthesis in the declaration of a function
  - ...Interesting stylistic choice, but the space between the function name and left parenthesis distinguishes functions from conditional statements

## Function-Like Macros

- Write functions instead of parameterized macros
- If you need to use a parameterized macro:
  - Surround macro body w/ parenthesis
  - Surround each use of the parameter w/ parenthesis
  - Use each parameter no more than once to avoid side effects
  - Never include transfer control (`return`, etc)

## Hardware Specific Features

- > To clearly define the rules in the rest of this standard, it is important that we first agree on the baseline programming language specification
- Avoid:
- `#pragma`
  - Macro to provide compiler specific instructions
  - Packing structs, etc
- Inline assembly code
  - Processor specific
- Preprocessor `#define` directive to rename any keyword / other aspects of the C programming language
  - So no, we shouldn't be masking integer data types to save a couple of processor cycles
  - If it really matters, it's a difference that should be encapsulated and isolated to a separate hardware specific module

## Header File Contents

- A header file should only identify procedures, constants, and data types which are strictly necessary for other modules to know
- Prefer not to declare variables w/ `extern` in a header file
- Don't allocate storage in header files

## Hungarian Notation

- BARR-C enforces hungarian notation below:
  - All public data types shall be prefixed w/ their module name and an underscore
  - Public functions shall be prefixed w/ their module name
  - Add postfix `_thread`/`_task`/`_process` to all functions that encapsulate threads of execution
  - Add postfix `_isr` to ISR implementations
  - Add prefix `g_`, `p_`, `pp_`, `b_`, `h_` for globals, pointers, pointers to pointers, booleans, and non-pointer handles for objects respectively
- As _Clean Code_ describes, hungarian notation is outdated
- Everything should be named descriptive enough to declare its purpose in its context
- No need to describe its form factor, or add context identifiers that don't need to be known

## Infinite Loops

- Implement infinite loops w/ `for (;;)`
- Better practice than `while (1)` as per K&R too, due to avoiding overlap w/ `while (l)`

## ISRs

- Make ISR's `static` to ensure they're not called elsewhere
- A stub or default ISR shall be installed in the vector table at the location of all unexpected or otherwise unhandled interrupt sources
  - The stubs should attempt to disable the interrupt

## Keywords to Avoid

- Avoid `auto` and `register`, and prefer to avoid `goto` and `continue`
- `auto` and `register` are good to understand just to know where variables are stored whenever optimization is a topic- otherwise they're archived keywords

## Keywords to Use

- `const`
  - Variables that don't change after initialization
  - Call by reference parameters that shouldn't be modified
  - Define `struct` / `union` that shouldn't be modified
- `static const` variables are the modern replacement of `#define`'s where `enum`'s aren't applicable
- ...As for function parameters
  - Making array parameters `const` introduces a confusing quirk about `const` pointers and distinguishing between keeping the value stored at the address constant and the address itself constant
  - Even if you use the right syntax to prevent the value stored at the address from changing, a developer can copy the pointer w/ a cast and start overwriting anyway
  - Code behavior like not writing input arrays should be verified w/ TDD

## LF Instead of CRLF

- End source code w/ `LF` instead of `CRLF`
  - Git enforces this automatically

## Line Width

- 80 characters, because code can be easily printed that way

## Main Files

- Modules containing `main()` should have `main` as a part of its source file name

## Multiple Return Statements

- Multiple return statements allowed if it improves readability

## Naming

- BARR-C enforces snake case- _Clean Code_ doesn't specify casing, because it's also just preference
  - No uppercase in function/variable names, underscores to separate words, each procedure name should be descriptive
- No variable name shall be shorter than 3 characters
  - _Clean Code_ admits that `i`, `j`, `k` aren't descriptive, but mentions they're conventional loop counters- they're fine

## Nesting Levels

- Don't nest deeper than two levels

## Pointer Operators and Spaces

- Use a space on each side of pointer operator `*` and `&` w/in declarations, but otherwise w/o a space on the operand side
  - Good practice, regardless of how BARR-C also enforces one variable declaration on each line

## Signed vs Unsigned

- Bitfields shall not be signed
- Bitwise operators shall not be used on signed data
- Signed integers shall not be combined w/ unsigned integers in comparisons or expressions

## Struct Union Padding

- Prevent the compiler from adding padding bytes in `struct`'s and `union`'s
- Prevent the compiler from altering the order of bits in bit-fields

## User Defined Types

- New data types should end w/ `_t`
  - Bad- POSIX has the `_t` postfix reserved for their standard portable data types

## Variable Declaration Location

- Define local variables where you need them instead of all at the top
- Project/file scope globals shall be grouped together
