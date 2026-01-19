# TDD C Specific

- C Specific TDD notes

## Index

- [Index](#index)
- [Handling Dependencies](#handling-dependencies)
- [Quick Tips](#quick-tips)

## Handling Dependencies

- Link time substitution
  - Used to replace an entire DOC with fakes/mocks
- Function pointers
  - Used to replace individual function calls (from DOC’s) in your interface with mocks/fakes
  - Extern a function pointer, replace calls to use function pointer, and reassign function pointer
- Preprocessor substitution
  - Avoid if possible
  - You can directly override function names in a file by doing
    - #define functionname mockfunctionname
  - Difficult to work w/, since changes cascade everywhere
- Spies (mocks with extra variables to track data passed to it)
  - Used to verify behavior going down to DOC’s (“depended on components”)
- Bare-bones fakes
  - Used when in need of certain output values from DOC’s to test an interface that’s being written
- CppUMock
  - Library designed for users to mock out dependencies when using CppUTest

## Quick Tips

- Use forward struct declarations to hide typedef internals in header files
- Use return statements as needed
  - If you write functions to be short and to adhere to single-responsibility principle, there will never be a crazy cluster of return statements
- Static file scope variables as a test doubles for hardware registers
  - A simple global file scope variable serves as a fake hardware register
