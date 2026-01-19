# Releases

- Releases of C++ notes

## Index

- [Index](#index)
- [C++ Releases](#c-releases)
- [Modern C++](#modern-c)

## C++ Releases

- C++98
  - Standardized the language w/ templates, exceptions, STL (“standard template library”)
- C++03
  - Bug fix release for C++98
- C++11
  - Smart pointers, auto, nullptr, lambda functions, move semantics, range-based for, multithreading support
- C++14
  - Generic lambdas, relaxed constexpr
- C++17
  - Std::optional, structured binding, and if constexpr
- C++20
  - Concepts, coroutines, ranges, modules
- C++23
  - Bug fixes, usability improvements, better library support

## Modern C++

- There's an emphasis on C++11 as a release, and for good reason
- C++11 introduces semantics and libraries that are crucial:
  - Move semantics
  - Smart pointers (`std::unique_ptr`, `std::shared_ptr`)
  - Lambda expressions
  - `auto` type deduction
  - Range-based for loops
  - `nullptr`
  - `constexpr`
  - Strongly-typed enums (`enum class`)
  - <thread> and real concurrency
  - `std::chrono`
  - Variadic templates
  - Type traits
  - Uniform initialization `{}`
- Just as C99 is crucial for C, C++11 provides safer and no-brainer semantics and features that you can't work without
- Modern libraries usually require C++11 too
