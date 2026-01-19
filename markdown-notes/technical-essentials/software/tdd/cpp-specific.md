# TDD C++ Specific

- C++ specific TDD notes

## Index

- [Index](#index)
- [Exceptions](#exceptions)
- [Writing Doubles](#writing-doubles)

## Exceptions

- What immediately comes to mind when incorporating TDD into C++ development is exceptions...
- Exceptions handle and propagate errors for when your specify that your code needs to behave that way to meet customer requirements (or design decisions)
  - Exceptions were never meant to be used in response to every precondition violation, edge case, etc
  - The developer needs to make design decisions to handle errors concisely
- Your unit tests then need to verify that behavior
  - In other words, verify that exceptions are thrown as desired, and caught/handled accordingly

## Writing Doubles

- There are bunch of ways to inject test doubles (mocks/fakes) in C++, but what's suggested is to use polymorphism
  - You can add spy logic by overriding virtual methods
  - This isn't applicable for concrete classes
  - This also means there's a vtable overhead
- Dependency inversion
  - If dependency inversion is implemented, then polymorphism would be valid
- Link-time substitution
  - Works just like in C
  - Works for concrete classes
- For troubles/complexities in getting some code to use the doubles, look into legacy code notes
  - Strategies include override factory, override getter, template parameters, etc
