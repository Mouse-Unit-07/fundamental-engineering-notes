# C++ Colon Overloading

- C++ colon token overloading notes

## Index

- [Index](#index)
- [Overview](#overview)
- [Access Specifiers in Classes](#access-specifiers-in-classes)
- [Enum Class Underlying Type](#enum-class-underlying-type)
- [Inheritance List](#inheritance-list)
- [Member Initializer List (Constructor Colon)](#member-initializer-list-constructor-colon)
- [Namespace / Class / Enum Scope Resolution](#namespace--class--enum-scope-resolution)
- [Range-Based `for` Loops](#range-based-for-loops)

## Overview

- In C, `:` is used for:
  - Bit-field width
  - Ternary operator separator
  - Labels (`case`, `goto`)
- C++ adds more meaning- below list helps sanity check what the tokens mean

## Access Specifiers in Classes

```
class X {
public:
    void f();

private:
    int x;
};
```

## Enum Class Underlying Type

```
enum class Color : uint8_t { Red, Green };
enum Days : int { Mon, Tue };
```

## Inheritance List

```
// single inheritance
class Derived : public Base {
};

// multiple inheritance
class D : public B1, private B2 {};
```

## Member Initializer List (Constructor Colon)

```
class A {
    int x;
public:
    A(int v) : x(v) {}   // colon introduces member initializer list
};
```

## Namespace / Class / Enum Scope Resolution

- The double colon "::" is a single token

```
// namespaces
std::vector<int> v;

// class static members
Widget::count = 10;

// enum class members
Color c = Color::Red;

// global scope qualification
::printf("global printf");
```

## Range-Based `for` Loops

```
for (auto x : container) {  }
```
