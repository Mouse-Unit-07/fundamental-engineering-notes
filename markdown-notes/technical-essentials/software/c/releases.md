# Releases

- Releases of C notes

## Index

- [Index](#index)
- [1989/90: ANSI C / C89 / C90](#198990-ansi-c--c89--c90)
- [1995: C95](#1995-c95)
- [1999: C99](#1999-c99)
- [2011: C11](#2011-c11)
- [2017/18: C17, sometimes called C18](#201718-c17-sometimes-called-c18)
- [2023: C23](#2023-c23)
- [GCC Version Number](#gcc-version-number)
- [K & R C](#k--r-c)

## 1989/90: ANSI C / C89 / C90

- C programming language standardized by ANSI
- In general we want to write code to follow ANSI C so that code is portable and compatible with all other C code
  - ...Now C99 is "ANSI C", but "ANSI C" as a term is thrown around to refer to C90
- International adoption of ANSI C
- Minor corrections

## 1995: C95

- Amendment to C90- wchar_t, wide characters, diagraphs, some library additions

## 1999: C99

- Major revision in C programming language on top of ANSI C that introduced:
- **Single-line comments**
  - This is why we comment using /\*\*/
- **Variable declarations in `for` loops**
  - Aka variable declarations mixed w/ statements
- **Variable array lengths**
  - Arrays can have sizes determined at runtime instead of compile time
- **Initialize specific members of struct/array**
  - Designated initializer syntax allows this
  - Write functions to initialize structs instead, and use memset to init arrays
- **Complex numbers**
  - For arithmetic operations
- **Bool data type**
  - Use sparingly (as in, use it when you need the boolean true/false as opposed to needing some other binary data structure)
- **Stdint.h and inttypes.h**
  - Critical issue w/ ANSI C
  - Would have to replicate stdint.h if this issue is encountered
- **Inline functions**
  - This is a keyword to suggest the compiler to directly inject the function’s code into the caller’s code during compile time, instead of generating a separate function call
  - A compiler can decide that the speed gained from injecting the function directly instead of creating a function call isn’t worth it, if the function is too large and takes up a lot of memory
  - Use sparingly
- **Restrict keyword**
  - Aka `__restrict` keyword in ANSI C
  - “Pointer qualifier” to indicate to the compiler that a pointer is the only reference to the object it points to (at least w/in the scope where the pointer is used)
  - Assumption that no other pointer will modify/access the same memory location allows the compiler to make optimizations
  - Don’t use them

## 2011: C11

- Major revision in C programming language on top of C99 that introduced:
- **Atomic operations**
  - Ensure that a set of operations are not interrupted by threads
- **Thread support library**
  - Functions written for thread creation, joining, and synchronization
- **Static assertions**
  - Validate certain conditions at compile time
- **Alignof and alignas**
  - Alignof- Provides info about alignment requirement of datatype
  - Alignas- specifies alignment of variables
- **Noreturn attribute**
  - Indicates that a function doesn’t return
- **Type `_generic` keyword**
  - Allows selection of expression/statements based on type of expression?
- **Memory alignment functions**
  - Functions to check dynamic memory allocation and checking alignment (“aligned_alloc” and “aligned_offset_malloc” respectively)
- **Unicode character literals**
  - Can use Unicode chars in character and string literals

## 2017/18: C17, sometimes called C18

- Bugfixes/clarifications to C11
- No major new features

## 2023: C23

- Added nullptr keyword like C++
- New safer string functions
- More modern usability improvements

## GCC Version Number

- `gcc` 3.x
  - Supports C90
- `gcc` 4.x, gcc 5.x
  - Supports C99 and basic C11
- `gcc` 8.x
  - Full C11 support and C17
- `gcc` 13.x+
  - Starts to implement C23

## K & R C

- First edition in 1972
- Second edition in 1978
