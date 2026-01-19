# C++ Templates

- C++ templates notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Example Usage](#example-usage)
- [Name Binding](#name-binding)
- [Specialization](#specialization)
- [Variants](#variants)

## Overview

- Templates in C++ allow for generic programming
- It's C++'s implementation of a generic/parameterized type
- Templates provide "compile-time polymorphism", as opposed to virtual functions that provide "run-time polymorphism"
- Allows for:
  - Compile-time polymorphism
  - Type-safe code reuse
  - Reduction of code duplication
- Best practices in the scope of generic programming:
  - Prefer template specialization just when behavior has to differ for specific types
  - Keep templates header-only to avoid linker errors

## Example Usage

```
#include <iostream>
#include <string>

// 1. Function template
template<typename T>
T myMax(const T& a, const T& b) {
    return (a > b) ? a : b;
}

// 2. Class template
template<typename T>
class Box {
private:
    T content;
public:
    Box(T c) : content(c) {}

    T getContent() const { return content; }

    void setContent(T c) { content = c; }
};

// 3. Non-type template parameter
template<int N>
class Array {
private:
    int data[N];
public:
    int& operator[](int i) { return data[i]; }
};

// 4. Template specialization
template<>
class Box<std::string> {
private:
    std::string content;
public:
    Box(std::string c) : content(c) {}
    void print() const { std::cout << "String Box: " << content << "\n"; }
};

int main() {
    // Function template
    std::cout << myMax(3, 7) << "\n";        // int
    std::cout << myMax(3.5, 2.1) << "\n";    // double
    std::cout << myMax(std::string("a"), std::string("b")) << "\n"; // string

    // Class template
    Box<int> intBox(42);
    std::cout << "Box<int>: " << intBox.getContent() << "\n";

    Box<std::string> strBox("Hello");
    strBox.print(); // specialized behavior

    // Non-type template parameter
    Array<5> arr;
    for(int i=0;i<5;++i) arr[i] = i*i;
    for(int i=0;i<5;++i) std::cout << arr[i] << " ";
    std::cout << "\n";

    return 0;
}
```

## Name Binding

- Refers to the process of finding the declaration for each name explicitly or implicitly used in a template

## Specialization

- A version of a template for a specific template argument is called a "specialization"

## Variants

- Function templates
  - Generic functions
- Class templates
  - Generic classes
- Template parameters
  - Can be types or non-types (integer constants, etc)
- Template specialization
  - Customize behavior for specific types
- Variadic templates
  - Support variable number of template parameters
